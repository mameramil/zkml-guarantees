"""Shared utilities for zkml-guarantees experiments."""
import json
import os
import platform
import subprocess
import time
from datetime import datetime
from pathlib import Path

RESULTS_DIR = Path("../../results")  # relative to experiment dirs
RESULTS_DIR.mkdir(exist_ok=True)

def capture_env():
    """Capture environment info as required by Section 8.6."""
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "platform": platform.platform(),
        "cpu": platform.processor() or "unknown",
        "python": platform.python_version(),
        # TODO: docker commit, library versions
    }

def write_result(experiment: str, data: dict, seed: int = 42):
    """Write results as JSON with fixed seed recorded."""
    data["seed"] = seed
    data["env"] = capture_env()
    data["experiment"] = experiment
    out = RESULTS_DIR / f"{experiment}_{int(time.time())}.json"
    with open(out, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {out}")
    return out

def run_docker(cmd: list, cwd: str = None):
    """Helper to run Docker commands (placeholder)."""
    print(f"[DOCKER] {' '.join(cmd)}")
    # TODO: actual subprocess.run with check=True, capture_output=True
    return {"returncode": 0, "stdout": "", "stderr": ""}
