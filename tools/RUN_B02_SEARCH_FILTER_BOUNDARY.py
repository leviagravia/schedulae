#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations
import os
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "tools" / "B02_GTK_LANE.py"

def main() -> int:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    current = env.get("G_DEBUG", "")
    env["G_DEBUG"] = ",".join(filter(None, (current, "fatal-criticals")))
    print("B02_R2_FOCUSED_BOUNDARY=search-filter")
    print("FOCUSED_GTK_LANES=1")
    result = subprocess.run(
        [sys.executable, str(LANE), "search-filter"],
        cwd=str(ROOT), env=env, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    print(result.stdout, end="")
    if result.returncode != 0:
        print("B02_R2_FOCUSED_BOUNDARY_RESULT=FAIL")
        print(f"ERR=search-filter:{result.returncode}")
        print("FINAL_PHASE=B02_R2_FOCUSED_SEARCH_FILTER_FAIL")
        return result.returncode or 1
    print("B02_R2_FOCUSED_BOUNDARY_RESULT=PASS")
    print("EXIT=0")
    print("ERR=NONE")
    print("FINAL_PHASE=B02_R2_FOCUSED_SEARCH_FILTER_PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
