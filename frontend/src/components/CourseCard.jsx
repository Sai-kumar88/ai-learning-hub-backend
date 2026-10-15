import React from "react";
import { Clock, Award, ExternalLink, BookOpen } from "lucide-react";

export default function CourseCard({ course }) {
  return (
    <div className="course-card">
      <div>
        <div className="course-card-top">
          <span className="provider-badge">
            {course.provider || "AI Learning"}
          </span>
          <span className="badge-catalog-type">
            <BookOpen size={12} />
            <span>Online Course</span>
          </span>
        </div>

        <h3 className="course-title">{course.course_name}</h3>

        <div className="course-meta">
          <div className="meta-item">
            <Clock size={15} color="var(--accent-secondary)" />
            <span>{course.duration || "Self-paced"}</span>
          </div>

          <div className="meta-item">
            <Award size={15} color="var(--accent-primary)" />
            <span>Certificate: {course.certificate || "Included"}</span>
          </div>
        </div>
      </div>

      <div className="course-actions">
        <a 
          href={course.course_url} 
          target="_blank" 
          rel="noopener noreferrer"
          className="btn-primary"
          style={{ width: "100%", justifyContent: "center" }}
        >
          <span>Start Learning</span>
          <ExternalLink size={16} />
        </a>
      </div>
    </div>
  );
}

