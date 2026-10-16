import json
import logging
from typing import List, Dict, Any, Optional
from config import Config

logger = logging.getLogger(__name__)

# Fallback course data in case data file is inaccessible in serverless container
FALLBACK_COURSES: List[Dict[str, Any]] = [
    {
        "id": 1,
        "course_name": "Claude 101",
        "provider": "Anthropic",
        "duration": "2.5 Hours",
        "certificate": "Yes",
        "course_url": "https://anthropic.skilljar.com/claude-101"
    },
    {
        "id": 2,
        "course_name": "AI Fluency: Framework & Foundations",
        "provider": "Anthropic",
        "duration": "3-4 Hours",
        "certificate": "Yes",
        "course_url": "https://anthropic.skilljar.com/ai-fluency-framework-foundations"
    }
]

def get_all_courses() -> List[Dict[str, Any]]:
    """
    Retrieve all courses from the JSON data repository.
    Falls back to built-in course catalog if file cannot be read.

    Returns:
        List[Dict[str, Any]]: List of course records.
    """
    courses_file = Config.COURSES_FILE

    if not courses_file.exists():
        logger.warning("Courses file not found at %s. Using default catalog.", courses_file)
        return FALLBACK_COURSES

    try:
        with open(courses_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) and len(data) > 0 else FALLBACK_COURSES
    except Exception as err:
        logger.error("Error reading courses repository: %s. Using fallback.", err)
        return FALLBACK_COURSES

def get_course_by_id(course_id: int) -> Optional[Dict[str, Any]]:
    """
    Find a single course by its unique identifier.

    Args:
        course_id (int): Unique ID of the course.

    Returns:
        Optional[Dict[str, Any]]: Course record if found, None otherwise.
    """
    courses = get_all_courses()
    return next((c for c in courses if c.get("id") == course_id), None)