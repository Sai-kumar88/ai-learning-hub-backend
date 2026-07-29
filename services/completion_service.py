import json
import os
from datetime import datetime
from config import Config

FILE_PATH = os.path.join(Config.DATA_FOLDER, "completed_courses.json")


def mark_course_completed(employee_id, course_id, certificate_url):

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Prevent duplicate completion
    for item in data:
        if (
            item["employee_id"] == employee_id
            and item["course_id"] == course_id
        ):
            return {
                "status": "error",
                "message": "Course already marked as completed."
            }

    data.append({
        "employee_id": employee_id,
        "course_id": course_id,
        "certificate_file": f"{employee_id}_{course_id}.pdf",
        "certificate_url": certificate_url,
        "status": "Completed",
        "completed_date": datetime.now().strftime("%Y-%m-%d")
    })

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return {
        "status": "success",
        "message": "Course marked as completed successfully."
    }


def get_completed_courses():
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)