"""Flask application for the Vaps AI Learning Center."""

import os
import threading
import webbrowser

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from config import Config
from routes.courses import course_bp
from services.course_service import get_all_courses
from utils.response import error_response


def _is_api_request(path: str) -> bool:
    """Return whether a request targets an API endpoint."""
    return any(
        path == prefix or path.startswith(f"{prefix}/")
        for prefix in ("/api", "/courses")
    )


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(
        __name__,
        template_folder=str(Config.TEMPLATES_DIR),
        static_folder=str(Config.STATIC_DIR),
        static_url_path="/static",
    )
    app.config.from_object(Config)

    CORS(app)

    app.register_blueprint(course_bp)
    app.register_blueprint(course_bp, name="api_course_bp", url_prefix="/api")

    @app.get("/")
    @app.get("/api/index")
    def home():
        return render_template("index.html", courses=get_all_courses())

    @app.get("/api")
    @app.get("/api/")
    def api_root():
        return jsonify(
            status="success",
            message="Vaps Artificial Intelligence Learning Center API",
            endpoints={
                "home": "/",
                "courses": "/courses or /api/courses",
                "health": "/api/health",
            },
        )

    @app.get("/health")
    @app.get("/api/health")
    def api_health():
        return jsonify(
            status="success",
            message=(
                "Vaps Artificial Intelligence Learning Center Backend "
                "Running Successfully"
            ),
        )

    @app.errorhandler(404)
    def handle_not_found(_error):
        if _is_api_request(request.path):
            return error_response("Endpoint or resource not found", status_code=404)
        return render_template("index.html", courses=get_all_courses()), 404

    @app.errorhandler(500)
    def handle_server_error(_error):
        if _is_api_request(request.path):
            return error_response("Internal server error", status_code=500)
        return render_template("index.html", courses=get_all_courses()), 500

    return app


# WSGI entry point used by production servers and Vercel.
app = create_app()


def _open_local_browser() -> None:
    """Open the local site when running the development server directly."""
    webbrowser.open(f"http://127.0.0.1:{Config.PORT}")


def main() -> None:
    """Run Flask's development server for local use."""
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        threading.Timer(1.2, _open_local_browser).start()

    print(
        "\n"
        "============================================================\n"
        "  Vaps Artificial Intelligence Learning Center is running!\n"
        f"  URL: http://127.0.0.1:{Config.PORT}\n"
        "============================================================\n"
    )
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)


if __name__ == "__main__":
    main()
