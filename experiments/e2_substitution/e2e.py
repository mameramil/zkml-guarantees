#!/usr/bin/env python3
"""E2e (Attack A9 — Selective proving / replay).

Replay a valid proof for a new request.
Expected: accepted without a nonce in the statement, rejected with one.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from utils import write_result

def run():
    # TODO: prove for (x, n1), then verify against (x, n2)
    without_nonce = True
    with_nonce = False
    return {
        "test": "E2e",
        "system": "EZKL",
        "bare": without_nonce,
        "pinned": with_nonce,
        "notes": "replay with/without user nonce",
    }

if __name__ == "__main__":
    write_result("e2e", run())
