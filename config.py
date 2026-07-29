import os

class Config:
    DEBUG = True
    JSON_SORT_KEYS = False

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_FOLDER = os.path.join(BASE_DIR, "data")

    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")