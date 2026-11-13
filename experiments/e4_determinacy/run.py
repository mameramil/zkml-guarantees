#!/usr/bin/env python3
"""E4 — Functional determinacy.

Take an honest witness, perturb the advice values of rescaling and nonlinear
steps by ±1 (and, where applicable, propagate the change), and check whether
the constraint system still accepts, using EZKL’s mock prover.
Any accepted perturbation shows that the circuit is at level F0 for that step.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from utils import write_result

def run():
    # TODO: load witness, perturb rescaling/nonlinear advice ±1, mock prove
    accepted_perturbations = []
    return {
        "test": "E4",
        "accepted_perturbations": accepted_perturbations,
        "level": "F0" if accepted_perturbations else "F1+",
    }

if __name__ == "__main__":
    write_result("e4_determinacy", run())
