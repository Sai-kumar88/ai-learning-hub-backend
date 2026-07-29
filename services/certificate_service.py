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

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    filename = f"{employee_id}_{course_id}.pdf"

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    certificate.save(filepath)

    return {
        "status": "success",
        "message": "Certificate uploaded successfully.",
        "file_name": filename
    }