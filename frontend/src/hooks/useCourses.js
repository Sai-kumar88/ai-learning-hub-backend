import { useState, useEffect, useMemo, useCallback } from "react";
import { fetchCourses } from "../services/api";

/**
 * Custom React hook for managing course catalog data, search, and filtering.
 * 
 * Provides:
 * - Real-time client-side search by title or provider
 * - Provider filter selection
 * - Safe async loading with error handling and unmount cleanup
 */
export function useCourses() {
  const [courses, setCourses] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Filters state
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedProvider, setSelectedProvider] = useState("all");

  const loadData = useCallback(async (signal) => {
    setIsLoading(true);
    setError(null);

    try {
      const data = await fetchCourses(signal);
      setCourses(data);
    } catch (err) {
      if (err.name === "AbortError") return;
      console.error("Course fetch error:", err);
      setError("Unable to connect to the backend server. Please verify your backend server is running.");
    } finally {
      setIsLoading(false);
    }
  }, []);

  // Initial load with cleanup
  useEffect(() => {
    const controller = new AbortController();
    loadData(controller.signal);
    return () => controller.abort();
  }, [loadData]);

  // Extract unique sorted provider names
  const providers = useMemo(() => {
    const set = new Set();
    courses.forEach((course) => {
      if (course?.provider) set.add(course.provider);
    });
    return Array.from(set).sort();
  }, [courses]);

  // Compute filtered courses based on query and provider
  const filteredCourses = useMemo(() => {
    const normalizedQuery = searchQuery.trim().toLowerCase();

    return courses.filter((course) => {
      const name = (course.course_name || "").toLowerCase();
      const provider = (course.provider || "").toLowerCase();

      const matchesSearch =
        !normalizedQuery ||
        name.includes(normalizedQuery) ||
        provider.includes(normalizedQuery);

      const matchesProvider =
        selectedProvider === "all" || course.provider === selectedProvider;

      return matchesSearch && matchesProvider;
    });
  }, [courses, searchQuery, selectedProvider]);

  // Helper to reset all search & filter parameters
  const clearFilters = useCallback(() => {
    setSearchQuery("");
    setSelectedProvider("all");
  }, []);

  // Helper to manually refresh courses from backend
  const reloadCourses = useCallback(() => {
    return loadData();
  }, [loadData]);

  return {
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
  };
}
