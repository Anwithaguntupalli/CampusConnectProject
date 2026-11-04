#!/usr/bin/env python3
"""
CampusConnect Server Launcher
Redirects execution to the full FastAPI backend in campusconnect-backend.
"""

import sys
import os
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = CURRENT_DIR.parent / "campusconnect-backend"

if BACKEND_DIR.exists() and (BACKEND_DIR / "run.py").exists():
    sys.path.insert(0, str(BACKEND_DIR))
    os.chdir(str(BACKEND_DIR))
    import run
    run.print_banner()
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)
else:
    print(f"Backend directory not found at {BACKEND_DIR}")
    sys.exit(1)
