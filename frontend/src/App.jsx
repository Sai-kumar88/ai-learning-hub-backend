import React from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import CourseGrid from "./components/CourseGrid";
import ErrorBanner from "./components/ErrorBanner";
import { useCourses } from "./hooks/useCourses";

/**
 * Main Application Component
 * Orchestrates the Vaps Artificial Intelligence Learning Center catalog layout.
 */
export default function App() {
  const { courses, isLoading, error, reloadCourses } = useCourses();

  return (
    <>
      {/* Brand Header */}
      <Navbar />

      {/* Hero Banner */}
      <Hero />

      {/* Main Catalog View */}
      <main className="main-container">
        {/* Backend Connectivity Error Alert */}
        <ErrorBanner message={error} onRetry={reloadCourses} />

        {/* Dynamic Courses Grid */}
        <CourseGrid courses={courses} isLoading={isLoading} />
      </main>

      {/* Minimal Footer */}
      <footer className="footer">
        <p>
          Vaps Artificial Intelligence Learning Center &bull; Curated Learning Resources &bull; Powered by Flask & React
        </p>
      </footer>
    </>
  );
}
