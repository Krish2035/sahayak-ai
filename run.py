"""
Sahayak AI Root Launcher
Run this single file from the root directory to start the full application.
Usage:
    python run.py
"""

import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(root_dir, "backend")

# Ensure backend directory is in sys.path
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import uvicorn
from app.config import HOST, PORT

if __name__ == "__main__":
    print("\n" + "=" * 65)
    print("👵👴 Sahayak AI: Digital Companion for Seniors is Starting!")
    print(f"👉 Open your browser to: http://{HOST}:{PORT}")
    print("=" * 65 + "\n")
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True, app_dir=backend_dir)

