"""Read-only source receipt checks and exact tracked-package fingerprints.

No integration action is performed. A passing receipt checks recorded evidence and
Git identity; it does not establish reviewer quality, authorization, or test efficacy.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


SHA = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
STATES = {"draft", "ready", "blocked", "superseded", "integrated"}


def git(root, *args):
    return subprocess.check_output(
        ["git", "-C", str(root), *args], encoding="utf-8"
    ).strip()


def identity(root, ref):
    # End-of-options prevents an externally supplied ref from becoming an option.
    commit = git(root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}")
    return {"commit": commit, "tree": git(root, "rev-parse", f"{commit}^{{tree}}")}


def validate_receipt(receipt, observed=None, integrated=None):
    errors = []
    if not isinstance(receipt, dict):
        return ["receipt must be an object"]
    state = receipt.get("state")
    if state not in STATES:
        errors.append("unknown receipt state")
    source = receipt.get("source")
    if not isinstance(source, dict) or any(
        not isinstance(source.get(key), str) or not SHA.fullmatch(source[key])
        for key in ("commit", "tree")
    ):
        return errors + ["source needs full commit and tree hashes"]
    if observed is not None and observed != source:
        errors.append("observed candidate differs from receipt source")
    if state in {"blocked", "superseded"}:
        errors.append(f"candidate is {state}; integration must stop")
    if state == "draft":
        errors.append("draft is incomplete; integration must stop")
    if state not in {"ready", "integrated"}:
        return errors
    for role in ("tested", "reviewed"):
        evidence = receipt.get(role)
        if not isinstance(evidence, dict) or evidence.get("source") != source:
            errors.append(f"{role} source differs or is missing")
        elif not isinstance(evidence.get("artifact"), str) or not evidence["artifact"].strip():
            errors.append(f"{role} artifact is missing")
    authorization = receipt.get("authorization", {})
    if not isinstance(authorization, dict) or (
        authorization.get("status") != "granted"
        or authorization.get("source") != source
        or authorization.get("action") != "integrate"
        or not authorization.get("evidence")
    ):
        errors.append("source-specific integration authorization is missing or denied")
    findings = receipt.get("findings")
    if not isinstance(findings, list):
        errors.append("finding dispositions are missing")
    else:
        for finding in findings:
            if not isinstance(finding, dict) or (
                not finding.get("id") or not isinstance(finding.get("blocking"), bool)
                or finding.get("status") not in {"open", "resolved", "deferred"}
                or not finding.get("evidence")
            ):
                errors.append("invalid finding disposition")
            elif finding["blocking"] and finding["status"] != "resolved":
                errors.append(f"unresolved blocking finding: {finding['id']}")
    checks = receipt.get("checks")
    if not isinstance(checks, list) or not checks:
        errors.append("verification checks are missing")
    else:
        for check in checks:
            if not isinstance(check, dict) or not check.get("command") or (
                check.get("outcome") != "passed" or not check.get("artifact")
            ):
                errors.append("verification check failed or lacks evidence")
    if state == "integrated":
        result = receipt.get("integration")
        if not isinstance(result, dict) or (
            result.get("candidate") != source or not result.get("artifact")
            or not isinstance(result.get("commit"), str)
            or not SHA.fullmatch(result["commit"])
            or result.get("tree") != source["tree"]
        ):
            errors.append("integration identity/evidence differs or is missing")
        elif integrated is not None and integrated != {
            "commit": result["commit"], "tree": result["tree"]
        }:
            errors.append("observed integration differs from recorded integration")
    elif integrated is not None:
        errors.append("integration observed without an integrated receipt")
    return errors


def package_inventory(root, paths):
    root = Path(root).resolve()
    files = {}
    for name in sorted(set(paths)):
        relative = Path(name)
        path = root / relative
        if relative.is_absolute() or not path.resolve().is_relative_to(root) or path.is_symlink():
            raise ValueError(f"unsafe package path: {name}")
        files[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    payload = json.dumps(files, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {"format": "sha256-raw-bytes-v1", "files": files,
            "digest": hashlib.sha256(payload).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    check = sub.add_parser("check")
    check.add_argument("receipt", type=Path)
    check.add_argument("--repo", type=Path, required=True)
    check.add_argument("--candidate", default="HEAD")
    check.add_argument("--integrated")
    fingerprint = sub.add_parser("inventory")
    fingerprint.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    if args.mode == "inventory":
        if git(args.repo, "status", "--porcelain", "--untracked-files=normal"):
            parser.error("inventory requires a clean committed source")
        names = git(args.repo, "ls-files", "-z").split("\0")
        result = package_inventory(args.repo, [name for name in names if name])
        result["source"] = identity(args.repo, "HEAD")
        result["version"] = json.loads((args.repo / "plugin.json").read_text(encoding="utf-8"))["version"]
        print(json.dumps(result, indent=2))
    else:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8-sig"))
        errors = validate_receipt(
            receipt, identity(args.repo, args.candidate),
            identity(args.repo, args.integrated) if args.integrated else None,
        )
        if git(args.repo, "status", "--porcelain", "--untracked-files=normal"):
            errors.append("working source is dirty; reconcile ownership and source evidence")
        print(json.dumps({"errors": errors, "passed": not errors}, indent=2))
        raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
