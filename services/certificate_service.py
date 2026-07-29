import cloudinary.uploader

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

    try:

        result = cloudinary.uploader.upload(
            certificate,
            resource_type="raw",
            folder="certificates",
            public_id=f"{employee_id}_{course_id}"
        )

        return {
            "status": "success",
            "message": "Certificate uploaded successfully.",
            "file_name": f"{employee_id}_{course_id}.pdf",
            "certificate_url": result["secure_url"]
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }