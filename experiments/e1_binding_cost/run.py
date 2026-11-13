#!/usr/bin/env python3
"""E1 — Cost of binding modes (Section 8.5).

For each width d and EZKL param_visibility mode, record:
- circuit rows (2^logrows)
- setup / prove / verify time
- proof size, verification-key size
- peak memory
Five repetitions; report median and IQR.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from utils import write_result, run_docker

DS = [16, 32, 64, 128]
MODES = ["private", "fixed", "hashed/public", "polycommit"]
REPS = 5
SEED = 42

def measure_mode(d: int, mode: str) -> dict:
    # TODO: generate tiny model of width d, export ONNX
    # TODO: docker run ezkl with pinned commit e196b11
    #   ezkl gen-settings / setup / prove / verify
    # Measure wall-clock, peak RSS, sizes
    print(f"Measuring d={d} mode={mode}")
    return {
        "d": d,
        "mode": mode,
        "logrows": None,  # tbd
        "setup_s": None,
        "prove_s": None,
        "verify_ms": None,
        "proof_kb": None,
        "vk_kb": None,
        "mem_gb": None,
        "reps": REPS,
    }

def main():
    results = []
    for d in DS:
        for mode in MODES:
            for rep in range(REPS):
                m = measure_mode(d, mode)
                m["rep"] = rep
                results.append(m)
    write_result("e1_binding_cost", {"measurements": results}, seed=SEED)

if __name__ == "__main__":
    main()
