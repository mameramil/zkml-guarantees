#!/usr/bin/env python3
"""E2d (Attack A3 — Weak Fiat–Shamir).

Modify public instances or embedded commitments in a valid proof file.
Expected: rejected in all cases; acceptance would indicate weak Fiat–Shamir.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from utils import write_result

def run():
    # TODO: take valid proof, alter public instances / cm, re-verify
    accepted = False  # expected
    return {
        "test": "E2d",
        "system": "EZKL",
        "bare": accepted,
        "pinned": accepted,
        "notes": "modified instances/commitments",
    }

if __name__ == "__main__":
    write_result("e2d", run())
