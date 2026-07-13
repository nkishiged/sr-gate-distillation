#!/usr/bin/env python3
"""Verify every archived artifact against the frozen SHA-256 manifest.

Usage:  python scripts/verify_checksums.py
Exit code 0 iff every file listed in checksums_sha256.json is present and
matches its recorded hash. This is the integrity gate referenced in the
manuscript's Data and code availability section.
"""
import json, hashlib, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "checksums_sha256.json")

def sha256(path, buf=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(buf), b""):
            h.update(block)
    return h.hexdigest()

def main():
    manifest = json.load(open(MANIFEST))
    ok, bad, missing = 0, [], []
    for rel, expected in sorted(manifest.items()):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            missing.append(rel)
        elif sha256(path) != expected:
            bad.append(rel)
        else:
            ok += 1
    print(f"verified : {ok}/{len(manifest)}")
    for r in missing:
        print(f"MISSING  : {r}")
    for r in bad:
        print(f"MISMATCH : {r}")
    sys.exit(0 if not bad and not missing else 1)

if __name__ == "__main__":
    main()
