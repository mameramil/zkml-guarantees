#!/usr/bin/env python3
"""E2c (Attack A4 — Descriptor substitution).

Keep the weights and their hash, change the scale or lookup range, and regenerate keys.
Expected: accepted if only the weight hash is pinned, rejected if the verification key is pinned.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from utils import write_result

def run():
    # TODO: same W, change κ (scale / LUT range), regenerate VK
    # Test with only H(cm) pinned vs full VK pinned
    return {
        "test": "E2c",
        "system": "EZKL hashed/public",
        "bare": None,
        "pinned": None,
        "notes": "descriptor change (scale/lookup)",
    }

if __name__ == "__main__":
    write_result("e2c", run())
