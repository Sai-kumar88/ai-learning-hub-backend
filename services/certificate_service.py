import os

UPLOAD_FOLDER = "uploads"

def upload_certificate(employee_id, course_id, certificate):

    if not employee_id or not course_id:
        return {
            "status": "error",
            "message": "Employee ID and Course ID are required."
        }

    if certificate is None:
        return {
            "status": "error",
            "message": "Please upload a certificate."
        }

    filename = certificate.filename

    return {
        "status": "success",
        "message": "Certificate received successfully.",
        "file_name": filename
    }