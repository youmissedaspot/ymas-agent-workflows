"""Small shared parser for visible Markdown lines, excluding fenced examples."""

import re


def visible_lines(contents):
    fence_char = None
    fence_size = 0
    for line in contents.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence_char is not None:
            if marker and marker[1][0] == fence_char and len(marker[1]) >= fence_size and not marker[2].strip():
                fence_char = None
            continue
        if marker:
            fence_char, fence_size = marker[1][0], len(marker[1])
            continue
        yield line
