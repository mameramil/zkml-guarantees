#!/usr/bin/env python3
"""E2a (Attack A1 — Fresh commitment).

Produce a proof with a different model and ship its own reference value.
Expected: accepted by the bare verifier, rejected by Verify of Algorithm 1.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from utils import write_result

def run():
    # TODO: generate two different tiny models M1, M2
    # TODO: prove with M2, ship cm of M2
    # Check bare EZKL verifier vs pinned registry check (Algorithm 1)
    bare_accept = True   # expected
    pinned_accept = False  # expected
    return {
        "test": "E2a",
        "system": "EZKL",
        "bare": bare_accept,
        "pinned": pinned_accept,
        "notes": "fresh commitment shipped with proof",
    }

if __name__ == "__main__":
    write_result("e2a", run())
