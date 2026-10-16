import sys
from pathlib import Path

# Ensure the root project directory is in the Python search path for Vercel
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app import app as flask_app

class VercelPathMiddleware:
    """
    WSGI middleware to normalize PATH_INFO for Vercel serverless deployment.
    Uses Vercel's HTTP_X_MATCHED_PATH to restore the original request path,
    or falls back to root / when /api/index is called directly.
    """
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        x_matched_path = environ.get("HTTP_X_MATCHED_PATH") or environ.get("HTTP_X_NOW_ROUTE_MATCHES")
        if x_matched_path:
            environ["PATH_INFO"] = x_matched_path.split("?")[0]
        elif environ.get("PATH_INFO") in ("/api/index", "/api/index/", "/api/index.py"):
            environ["PATH_INFO"] = "/"
        elif environ.get("PATH_INFO", "").startswith("/api/index/"):
            environ["PATH_INFO"] = environ["PATH_INFO"][len("/api/index"):]
            
        return self.wsgi_app(environ, start_response)

app = VercelPathMiddleware(flask_app)
