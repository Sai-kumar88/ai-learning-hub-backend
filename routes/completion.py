from flask import Blueprint, request
from services.completion_service import (
    mark_course_completed,
    get_completed_courses
)
from utils.response import success_response, error_response
completion_bp = Blueprint("completion_bp", __name__)

@completion_bp.route("/course/complete", methods=["POST"])
def complete_course():

    data = request.get_json()
    employee_id = data.get("employee_id")
    course_id = data.get("course_id")

    if not employee_id or not course_id:
        return error_response("employee_id and course_id are required")

    saved = mark_course_completed(employee_id, course_id)

    if not saved:
        return error_response("Course already marked as completed")

    return success_response(message="Course marked as completed")


@completion_bp.route("/course/completed", methods=["GET"])
def completed_courses():

    return success_response(
        data=get_completed_courses(),
        message="Completed courses fetched successfully"
    )