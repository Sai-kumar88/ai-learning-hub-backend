from flask import Blueprint, request, jsonify
from services.certificate_service import upload_certificate

certificate_bp = Blueprint("certificate", __name__)

@certificate_bp.route("/course/upload-certificate", methods=["POST"])
def upload():
    employee_id = request.form.get("employee_id")
    course_id = request.form.get("course_id")
    certificate = request.files.get("certificate")

    response = upload_certificate(employee_id, course_id, certificate)
    return jsonify(response)