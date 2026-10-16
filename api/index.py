import sys
from pathlib import Path

# Ensure the root project directory is in the Python search path for Vercel
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app import app
