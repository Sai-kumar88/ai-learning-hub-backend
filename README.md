# Vaps Artificial Intelligence Learning Center

A clean, modern, lightweight Flask web application and REST API for exploring curated Artificial Intelligence courses and learning resources from leading AI pioneers.

---

## 🌟 Overview

The **Vaps Artificial Intelligence Learning Center** is built with clean Python Flask and pure, semantic HTML5/CSS3. It provides a friction-free learning directory where users can browse world-class, accredited AI awareness courses, inspect actual curriculum durations and credentials, and launch directly into external course materials.

- **No Heavy Build Steps**: Pure HTML and CSS served directly by Flask — zero Node.js, npm, or bundler dependencies required.
- **Vercel-Ready**: Preconfigured with `vercel.json` and `api/index.py` serverless entry point for instant one-click deployment.
- **Responsive & Modern Design**: Clean glassmorphism styling, curated typography (Inter & Outfit), responsive CSS grid, and instant client-side course search.

---

## 📁 Project Structure

```text
ai-awareness-backend/
│
├── api/
│   └── index.py               # Vercel serverless function entrypoint
│
├── data/
│   └── courses.json           # Curated courses repository
│
├── routes/
│   ├── __init__.py
│   └── courses.py             # REST API endpoints (/courses, /courses/<id>)
│
├── services/
│   ├── __init__.py
│   └── course_service.py      # Course retrieval service with safe fallbacks
│
├── static/
│   ├── css/
│   │   └── style.css          # Clean, modern CSS styling
│   └── images/
│       ├── vaps_logo.png      # Official brand logo
│       ├── vaps_icon.png      # Brand favicon icon
│       └── ...
│
├── templates/
│   └── index.html             # Clean, semantic HTML5 Jinja2 template
│
├── utils/
│   ├── __init__.py
│   └── response.py            # Standardized JSON response utilities
│
├── app.py                     # Flask application factory and local dev server
├── config.py                  # Environment and directory configuration
├── requirements.txt           # Minimal Python dependencies
├── run.bat                    # One-click Windows launch script
└── vercel.json                # Vercel deployment routing configuration
```

---

## 🚀 Running Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Application
```bash
python app.py
```
Or on Windows, simply double-click `run.bat`.

The application will start at **`http://127.0.0.1:5000`** and open in your default browser.

---

## 🌐 Deploying to Vercel

### Method 1: Vercel CLI
```bash
# 1. Install Vercel CLI (if not installed)
npm i -g vercel

# 2. Deploy to preview
vercel

# 3. Deploy to production
vercel --prod
```

### Method 2: Git Integration (GitHub / GitLab / Bitbucket)
1. Push this repository to GitHub.
2. In the [Vercel Dashboard](https://vercel.com/dashboard), click **Add New Project** and import the repository.
3. Vercel automatically detects the Python project via `requirements.txt` and routes all traffic using `vercel.json` to `api/index.py`.
4. Click **Deploy**.

---

## 📡 REST API Endpoints

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/` | `GET` | Main course directory web page (HTML) |
| `/courses` | `GET` | List all available AI courses (JSON) |
| `/courses/<id>` | `GET` | Retrieve details for a specific course (JSON) |
| `/api/health` | `GET` | Service health status check |
