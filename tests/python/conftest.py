"""Ensure the in-tree Python package is importable when running pytest from the repo root."""

import os
import sys

_REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", ".."))
_GNOLL_PKG = os.path.join(_REPO_ROOT, "src", "python", "code")
if _GNOLL_PKG not in sys.path:
    sys.path.insert(0, _GNOLL_PKG)
