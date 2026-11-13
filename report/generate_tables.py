#!/usr/bin/env python3
"""Regenerate Tables 8.1 and 8.2 from results/*.json (Section 8.6)."""
import json
from pathlib import Path

RESULTS = Path("../results")

def main():
    # TODO: load all e1_*.json, compute median/IQR, emit markdown Table 8.1
    # TODO: load e2*.json, emit Table 8.2
    print("# Table 8.1 (placeholder)")
    print("# Table 8.2 (placeholder)")

if __name__ == "__main__":
    main()
