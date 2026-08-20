# SPDX-License-Identifier: GPL-3.0-or-later
"""Run the native Schedulae GTK application."""
from __future__ import annotations

import sys

from schedulae.gtk_app import run


if __name__ == "__main__":
    raise SystemExit(run(sys.argv))
