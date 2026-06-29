from flask import Blueprint
from services.course_service import get_all_courses
from utils.response import success_response

course_bp = Blueprint("course_bp", __name__)

@course_bp.route("/courses", methods=["GET"])
def get_courses():
    courses = get_all_courses()

    return success_response(
        data=courses,
        message="Courses fetched successfully"
    )