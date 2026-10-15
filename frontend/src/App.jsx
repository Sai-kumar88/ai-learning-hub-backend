import React from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import CatalogControls from "./components/CatalogControls";
import CourseGrid from "./components/CourseGrid";
import ErrorBanner from "./components/ErrorBanner";
import { useCourses } from "./hooks/useCourses";

/**
 * Main Application Component
 * Orchestrates the course catalog layout, data flow, and filtering.
 */
export default function App() {
  const {
    courses,
    filteredCourses,
    providers,
    isLoading,
    error,
    searchQuery,
    setSearchQuery,
    selectedProvider,
    setSelectedProvider,
    clearFilters,
    reloadCourses
  } = useCourses();

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

        {/* Search, Filter, and View Controls */}
        <CatalogControls
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          selectedProvider={selectedProvider}
          onProviderChange={setSelectedProvider}
          providers={providers}
          totalCourses={courses.length}
          filteredCount={filteredCourses.length}
          isLoading={isLoading}
          onRefresh={reloadCourses}
        />

        {/* Dynamic Courses Grid with Loading & Empty State */}
        <CourseGrid
          courses={filteredCourses}
          isLoading={isLoading}
          searchQuery={searchQuery}
          onClearFilters={clearFilters}
        />
      </main>

      {/* Minimal Footer */}
      <footer className="footer">
        <p>
          AI Course Catalog &bull; Curated Learning Resources &bull; Powered by Flask & React
        </p>
      </footer>
    </>
  );
}
