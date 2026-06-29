from flask import Flask
from flask_cors import CORS
from config import Config
from routes.courses import course_bp
from routes.completion import completion_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
app.register_blueprint(course_bp)
app.register_blueprint(completion_bp)

@app.route("/")
def home():
    return {
        "status": "success",
        "message": "Training Resource Backend Running Successfully"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)