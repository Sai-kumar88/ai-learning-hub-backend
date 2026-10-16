import os
import mimetypes
import webbrowser
import threading
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from config import Config
from routes.courses import course_bp
from utils.response import error_response

# Ensure proper Windows MIME type recognition for modern JS/CSS
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")

load_dotenv()

def create_app() -> Flask:
    """
    Application factory for the AI Course Catalog backend.
    
    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(
        __name__,
        static_folder=str(Config.FRONTEND_DIST),
        static_url_path=""
    )
    app.config.from_object(Config)

    # Enable CORS for cross-origin client apps
    CORS(app)

    # Register API Blueprints
    app.register_blueprint(course_bp)

    # Health Check API
    @app.route("/api/health", methods=["GET"])
    def api_health():
        return jsonify({
            "status": "success",
            "message": "Vaps Artificial Intelligence Learning Center Backend Running Successfully"
        })

    # Frontend Single Page Application & Static Assets
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve_frontend(path: str):
        dist_folder = Config.FRONTEND_DIST
        asset_file = dist_folder / path

        # Serve static asset from dist folder if it exists
        if path != "" and asset_file.is_file():
            return send_from_directory(str(dist_folder), path)

        # Serve React frontend index.html for root and client-side routing
        index_file = dist_folder / "index.html"
        if index_file.is_file():
            return send_from_directory(str(dist_folder), "index.html")


    # Global Error Handlers
    @app.errorhandler(404)
    def handle_not_found(e):
        if request.path.startswith("/api") or request.path.startswith("/courses"):
            return error_response("Endpoint or resource not found", status_code=404)
        
        index_file = Config.FRONTEND_DIST / "index.html"
        if index_file.is_file():
            return send_from_directory(str(Config.FRONTEND_DIST), "index.html")
        return error_response("Page not found", status_code=404)

    @app.errorhandler(500)
    def handle_server_error(e):
        return error_response("Internal server error", status_code=500)

    return app

# Application instance for WSGI / Vercel
app = create_app()

def open_browser():
    """Launch user's default browser on application startup."""
    try:
        webbrowser.open(f"http://127.0.0.1:{Config.PORT}")
    except Exception as err:
        print(f"Notice: Could not automatically open browser ({err})")

if __name__ == "__main__":
    # Prevent duplicate browser launches during development auto-reloads
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        threading.Timer(1.2, open_browser).start()

    print("\n" + "=" * 60)
    print("  Vaps Artificial Intelligence Learning Center is running!")
    print(f"  URL: http://127.0.0.1:{Config.PORT}")
    print("=" * 60 + "\n")

    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)