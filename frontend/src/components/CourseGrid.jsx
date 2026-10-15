import React from "react";
import { RotateCw, GraduationCap } from "lucide-react";
import CourseCard from "./CourseCard";

/**
 * Grid layout for rendering courses or loading/empty state.
 */
export default function CourseGrid({
  courses = [],
  isLoading = false
}) {
  // 1. Loading State
  if (isLoading) {
    return (
      <div style={{ textAlign: "center", padding: "4rem" }} role="status">
        <RotateCw
          size={36}
          className="animate-spin"
          color="var(--accent-primary)"
          style={{ margin: "0 auto 1rem" }}
          aria-hidden="true"
        />
        <p style={{ color: "var(--text-muted)" }}>Loading courses catalog...</p>
      </div>
    );
  }

  // 2. Empty State
  if (courses.length === 0) {
    return (
      <div className="empty-state">
        <div className="empty-icon">
          <GraduationCap size={32} aria-hidden="true" />
        </div>
        <h3 className="empty-title">No Courses Available</h3>
        <p className="empty-desc">
          No courses are currently available in the database.
        </p>
      </div>
    );
  }

  // 3. Grid of Course Cards
  return (
    <div className="courses-grid" role="list">
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} />
      ))}
    </div>
  );
}
