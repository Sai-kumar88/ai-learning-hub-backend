# AI Awareness 
## Overview

The AI Awareness Backend is a Flask-based REST API developed for the Training Module. It provides AI awareness course information and allows employees to mark external AI courses as completed.

Employees can access free AI learning resources, complete the courses on the provider's website, earn certificates, and update their completion status in the ERP.

---

# Features

* View available AI Awareness courses
* Open external AI learning links
* Mark a course as completed
* View completed course records
* Simple JSON-based storage
* REST APIs for frontend integration

---

# Project Structure

```text
training-resource-backend/
│
├── app.py
├── config.py
├── requirements.txt
│
├── routes/
│   ├── __init__.py
│   ├── courses.py
│   └── completion.py
│
├── services/
│   ├── __init__.py
│   ├── course_service.py
│   └── completion_service.py
│
├── data/
│   ├── courses.json
│   └── completed_courses.json
│
└── utils/
    ├── __init__.py
    └── response.py
```

---

# Installation

Clone the project.

```bash
git clone <repository-url>
```

Navigate to the project.

```bash
cd training-resource-backend
```

Create Virtual Environment.

```bash
python -m venv .venv
```

Activate Virtual Environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python app.py
```

Server runs at

```text
http://127.0.0.1:5000
```

---

# API Endpoints

## Health Check

### Request

```http
GET /
```

### Response

```json
{
    "status": "success",
    "message": "Training Resource Backend Running Successfully"
}
```

---

## Get All Courses

### Request

```http
GET /courses
```

### Response

```json
{
    "status": "success",
    "message": "Courses fetched successfully",
    "data": [
        {
            "id": 1,
            "course_name": "Claude 101",
            "provider": "Anthropic",
            "duration": "30-60 Minutes",
            "certificate": "Yes",
            "course_url": "https://www.anthropic.com/learn/claude-101"
        }
    ]
}
```

---

## Mark Course Completed

### Request

```http
POST /course/complete
```

### Request Body

```json
{
    "employee_id":"EMP001",
    "course_id":1
}
```

### Response

```json
{
    "status":"success",
    "message":"Course marked as completed"
}
```

---

## View Completed Courses

### Request

```http
GET /course/completed
```

### Response

```json
{
    "status":"success",
    "message":"Completed courses fetched successfully",
    "data":[
        {
            "employee_id":"EMP001",
            "course_id":1,
            "status":"Completed",
            "completed_date":"2026-06-27"
        }
    ]
}
```

---

# Frontend Integration Flow

1. Call **GET /courses** when the page loads.
2. Display all AI Awareness courses.
3. Clicking **Start Course** opens the external course URL.
4. After completing the course, the employee clicks **Mark as Completed**.
5. Frontend calls **POST /course/complete**.
6. HR/Admin can retrieve completion details using **GET /course/completed**.

---

# Data Storage

## courses.json

Stores all available AI awareness courses.

## completed_courses.json

Stores employee course completion records.

---

# Technologies Used

* Python 3.x
* Flask
* Flask-CORS
* JSON Storage
* Gunicorn

---

# Current AI Courses

| Course                              | Provider  | Duration      | Certificate |
| ----------------------------------- | --------- | ------------- | ----------- |
| Claude 101                          | Anthropic | 30–60 Minutes | Yes         |
| AI Fluency: Framework & Foundations | Anthropic | 1.1 Hours     | Yes         |

---

# Future Enhancements

* Database integration (MySQL/PostgreSQL)
* Employee authentication
* Certificate upload support
* Completion dashboard
* Course progress tracking
* Email notifications
* Admin analytics
* Search and filtering
* Course categories

---

AI Learning Hub Backend

Base URL
https://ai-learning-hub-backend.vercel.app

1. Get All Courses

Method: GET

API

GET https://ai-learning-hub-backend.vercel.app/courses

Purpose

Fetch all AI learning courses.
Display course name, provider, duration, certificate.
Open course_url when the employee clicks Start Course.

2.Mark Course as Completed

Method: POST

API

POST https://ai-learning-hub-backend.vercel.app/course/complete

Headers

Content-Type: application/json

Request Body

{
    "employee_id": "<LoggedInEmployeeID>",
    "course_id": 1
}

Example:

{
    "employee_id": "EMP001",
    "course_id": 1
}

3.Get Completed Courses

Method: GET

API

GET https://ai-learning-hub-backend.vercel.app/course/completed

# Developed For

Training Module – AI Awareness Program

This backend enables employees to discover AI learning resources, complete free certification courses, and maintain completion records within the organization's training system.
