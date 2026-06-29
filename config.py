import os
class Config:
    DEBUG = True
    JSON_SORT_KEYS = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_FOLDER = os.path.join(BASE_DIR, "data")