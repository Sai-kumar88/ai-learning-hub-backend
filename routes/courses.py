from flask import Blueprint
from services.course_service import get_all_courses, get_course_by_id
from utils.response import success_response, error_response

course_bp = Blueprint("course_bp", __name__)

@course_bp.route("/courses", methods=["GET"])
def get_courses():
    """
    Fetch all courses available in the catalog.
    
    Returns:
        JSON response with list of courses.
    """
    courses = get_all_courses()
    return success_response(
        data=courses,
        message="Courses fetched successfully"
    )

@course_bp.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id: int):
    """
    Fetch details for a single course by ID.

    Args:
        course_id (int): Course identifier.

    Returns:
        JSON response with course data or 404 error.
    """
    course = get_course_by_id(course_id)
    if not course:
        return error_response(
            message=f"Course with ID {course_id} not found",
            status_code=404
        )
    return success_response(
        data=course,
        message="Course retrieved successfully"
    )