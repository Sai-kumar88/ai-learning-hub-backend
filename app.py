from flask import Flask
from flask_cors import CORS
from config import Config
from routes.courses import course_bp
from routes.completion import completion_bp
from routes.certificate import certificate_bp

import cloudinary
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

cloudinary.config(
    cloud_name=app.config["CLOUDINARY_CLOUD_NAME"],
    api_key=app.config["CLOUDINARY_API_KEY"],
    api_secret=app.config["CLOUDINARY_API_SECRET"],
    secure=True
)

CORS(app)

app.register_blueprint(course_bp)
app.register_blueprint(completion_bp)
app.register_blueprint(certificate_bp)

@app.route("/")
def home():
    return {
        "status": "success",
        "message": "Training Resource Backend Running Successfully"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)