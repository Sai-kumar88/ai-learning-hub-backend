import json
import os
from config import Config

def get_all_courses():
    print("BASE_DIR :", Config.BASE_DIR)
    print("DATA_DIR :", Config.DATA_FOLDER)

    file_path = os.path.join(Config.DATA_FOLDER, "courses.json")

    print("FILE :", file_path)
    print("EXISTS :", os.path.exists(file_path))

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)