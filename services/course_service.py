import json
import logging
from typing import List, Dict, Any, Optional
from config import Config

logger = logging.getLogger(__name__)

def get_all_courses() -> List[Dict[str, Any]]:
    """
    Retrieve all courses from the JSON data repository.

    Returns:
        List[Dict[str, Any]]: List of course records, or empty list if unavailable.
    """
    courses_file = Config.COURSES_FILE

    if not courses_file.exists():
        logger.warning(f"Courses repository file not found at: {courses_file}")
        return []

    try:
        with open(courses_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError as err:
        logger.error(f"Error parsing JSON from courses repository: {err}")
        return []
    except Exception as err:
        logger.error(f"Unexpected error loading courses repository: {err}")
        return []

def get_course_by_id(course_id: int) -> Optional[Dict[str, Any]]:
    """
    Find a single course by its unique identifier.

    Args:
        course_id (int): Unique ID of the course.

    Returns:
        Optional[Dict[str, Any]]: Course record if found, None otherwise.
    """
    courses = get_all_courses()
    return next((course for course in courses if course.get("id") == course_id), None)