/**
 * Application Configuration
 * Provides dynamic API base resolution with environment variable override and local fallback.
 */

const DEFAULT_API_BASE = "https://ai-learning-hub-backend.vercel.app";
const LOCAL_API_BASE = "http://127.0.0.1:5000";

/**
 * Dynamically determines the backend API base URL based on runtime environment.
 * @returns {string} The base URL for API requests.
 */
export const getApiBaseUrl = () => {
  // 1. Check for Vite environment variable override
  if (typeof import.meta !== "undefined" && import.meta.env?.VITE_API_URL) {
    return import.meta.env.VITE_API_URL;
  }

  // 2. Check for manually saved local storage override
  if (typeof window !== "undefined") {
    const saved = localStorage.getItem("ai_hub_api_base");
    if (saved) return saved;

    // 3. When running under the same host/port (e.g., Flask serving frontend build on port 5000)
    if (window.location.port === "5000") {
      return window.location.origin;
    }

    // 4. When running on localhost / 127.0.0.1 in development
    if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") {
      return LOCAL_API_BASE;
    }
  }

  // 5. Default fallback to deployed cloud backend
  return DEFAULT_API_BASE;
};

export const API_ENDPOINTS = Object.freeze({
  COURSES: "/courses",
  HEALTH: "/api/health"
});

export { DEFAULT_API_BASE, LOCAL_API_BASE };
