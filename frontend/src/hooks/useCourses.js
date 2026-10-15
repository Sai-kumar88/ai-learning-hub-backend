import { useState, useEffect, useCallback } from "react";
import { fetchCourses } from "../services/api";

/**
 * Custom React hook for fetching and managing course catalog data.
 */
export function useCourses() {
  const [courses, setCourses] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

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

  // Helper to manually refresh courses from backend
  const reloadCourses = useCallback(() => {
    return loadData();
  }, [loadData]);

  return {
    courses,
    isLoading,
    error,
    reloadCourses
  };
}
