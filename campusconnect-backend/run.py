#!/usr/bin/env python3
"""
CampusConnect Unified Production Server Runner
Runs FastAPI backend on port 8000 with auto-reload and serves both API and Frontend.
"""

import os
import sys
import subprocess
from pathlib import Path

# Ensure current directory is in sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Ensure required dependencies are installed in the currently active Python interpreter
def ensure_dependencies():
    missing = []
    try:
        import uvicorn
    except ImportError:
        missing.append("uvicorn")
    try:
        import fastapi
    except ImportError:
        missing.append("fastapi")
    try:
        import sqlalchemy
    except ImportError:
        missing.append("sqlalchemy")

    if missing:
        req_file = BASE_DIR / "requirements.txt"
        print(f"\n[CampusConnect] Detected missing dependencies ({', '.join(missing)}) in:")
        print(f" -> Python: {sys.executable}\n")
        print(f"[*] Installing requirements automatically via {sys.executable} -m pip install...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
            print("\n[+] Dependencies successfully installed!\n")
        except Exception as e:
            print(f"\n[!] Automatic installation failed: {e}")
            print(f"Please install dependencies manually using:")
            print(f'   & "{sys.executable}" -m pip install -r requirements.txt\n')
            sys.exit(1)

ensure_dependencies()

import uvicorn

def print_banner():
    banner = r"""
 =====================================================================
   ____                                   ____                            _   
  / ___|__ _ _ __ ___  _ __  _   _ ___   / ___|___  _ __  _ __   ___  ___| |_ 
 | |   / _` | '_ ` _ \| '_ \| | | / __| | |   / _ \| '_ \| '_ \ / _ \/ __| __|
 | |__| (_| | | | | | | |_) | |_| \__ \ | |__| (_) | | | | | | |  __/ (__| |_ 
  \____\__,_|_| |_| |_| .__/ \__,_|___/  \____\___/|_| |_|_| |_|\___|\___|\__|
                      |_|                                                     
               -- Enterprise Event Management Backend Engine --
 =====================================================================
  * REST API Base URL:       http://localhost:8000/api
  * Interactive Swagger UI:  http://localhost:8000/docs
  * Interactive ReDoc:       http://localhost:8000/redoc
  * Fullstack Frontend UI:   http://localhost:8000/
 =====================================================================
    """
    print(banner)

if __name__ == "__main__":
    print_banner()
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )
