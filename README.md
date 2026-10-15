# Vaps Artificial Intelligence Learning Center

A clean, modern web platform and REST API for exploring curated Artificial Intelligence courses and learning resources from leading AI pioneers.

---

## 🌟 Overview

The **Vaps Artificial Intelligence Learning Center** provides a friction-free learning directory where users can browse world-class, accredited AI awareness courses, inspect actual curriculum durations and credentials, and launch directly into external course materials.

All tracking features, employee ID requirements, progress percentages, and certificate uploads have been eliminated to keep the platform simple, fast, and accessible to everyone.

---

## 🚀 Features

* **Curated Course Directory**: Browse AI awareness courses with verified curriculum duration, provider, and certification information.
* **One-Click Course Access**: Direct **Start Learning** links to external course materials.
* **Frictionless Experience**: Zero employee ID requirements, no login walls, and no completion tracking.
* **Responsive Modern Design**: Built with React and Vanilla CSS for high performance and visual polish.
* **All-in-One Deployment**: Flask serves both the REST API and the compiled React production frontend on `http://127.0.0.1:5000`.

---

## 📁 Project Structure

```text
ai-awareness-backend/
│
├── app.py                     # Flask application entry point & static file server
├── config.py                  # Application configuration
├── requirements.txt           # Python backend dependencies
├── run.bat                    # One-click Windows launch script
│
├── data/
│   └── courses.json           # Course catalog data store
│
├── routes/
│   ├── __init__.py
│   └── courses.py             # Courses REST endpoint (/courses)
│
├── services/
│   ├── __init__.py
│   └── course_service.py      # Course retrieval service logic
│
├── utils/
│   ├── __init__.py
│   └── response.py            # Standard JSON API response helper
│
└── frontend/                  # React + Vite frontend application
    ├── index.html             # HTML entry point
    ├── package.json           # Frontend dependencies & scripts
    ├── vite.config.js         # Vite bundler configuration
    ├── dist/                  # Compiled production build served by Flask
    └── src/
        ├── App.jsx            # Top-level orchestrator layout
        ├── index.css          # Core design system & responsive styling
        ├── config.js          # API base URL configuration
        ├── hooks/
        │   └── useCourses.js  # Custom hook for catalog data fetching
        ├── components/
        │   ├── Navbar.jsx     # Clean top header and branding
        │   ├── Hero.jsx       # Hero presentation banner
        │   ├── CourseGrid.jsx # Grid container with loading & empty states
        │   ├── CourseCard.jsx # Course card with direct launch link
        │   └── ErrorBanner.jsx# Connection error alert with retry action
        └── services/
            └── api.js         # Fetch client for courses API
```

---

## ⚡ Quick Start

### Option 1: One-Click Run (Windows)

Simply double-click `run.bat` in the project root:

```cmd
run.bat
```

This activates the virtual environment, launches the Flask server, and automatically opens your default web browser to `http://127.0.0.1:5000`.

---

### Option 2: Manual Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-awareness-backend
   ```

2. **Create and activate a virtual environment**:
   - **Windows**:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**:
   ```bash
   python app.py
   ```

5. **Open in browser**:
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 💻 Frontend Development (Vite Dev Server)

If you wish to run the frontend independently with hot module replacement (HMR):

```bash
cd frontend
npm install
npm run dev
```

The dev server will run at `http://localhost:5173/`.

To build updated production assets for Flask to serve:
```bash
npm run build
```

---

## 📡 API Reference

### 1. Health Check

```http
GET /api/health
```

**Response**:
```json
{
  "status": "success",
  "message": "Vaps Artificial Intelligence Learning Center Backend Running Successfully"
}
```

---

### 2. Get All Courses

```http
GET /courses
```

**Response**:
```json
{
  "status": "success",
  "message": "Courses fetched successfully",
  "data": [
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
}
```

---

## 📚 Current Courses Catalog

| ID | Course Name | Provider | Actual Duration | Certificate | URL |
|---|---|---|---|---|---|
| 1 | Claude 101 | Anthropic | 2.5 Hours | Yes | [Open Course](https://anthropic.skilljar.com/claude-101) |
| 2 | AI Fluency: Framework & Foundations | Anthropic | 3–4 Hours | Yes | [Open Course](https://anthropic.skilljar.com/ai-fluency-framework-foundations) |

---

## 🛠️ Technologies Used

* **Backend**: Python 3, Flask, Flask-CORS
* **Frontend**: React 19, Vite, Lucide Icons, Vanilla CSS Design System
* **Data Layer**: JSON storage (`data/courses.json`)
* **Serving**: Flask static routing serving compiled React SPA bundle
