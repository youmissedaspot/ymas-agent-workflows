"""Synthetic in-memory record lookup; no external state or application integration."""


def lookup(records, key):
    return records.get(key)
