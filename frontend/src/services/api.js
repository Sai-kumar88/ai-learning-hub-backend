/**
 * API Service Client
 * Handles HTTP communication with the AI Course Catalog REST backend.
 */

import { getApiBaseUrl, API_ENDPOINTS } from "../config";

/**
 * Checks backend API health and connectivity.
 * @returns {Promise<{ ok: boolean, data?: object, error?: string }>}
 */
export async function checkBackendHealth() {
  const baseUrl = getApiBaseUrl();
  try {
    const res = await fetch(`${baseUrl}${API_ENDPOINTS.HEALTH}`, {
      method: "GET",
      headers: { Accept: "application/json" }
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    return { ok: true, data };
  } catch (err) {
    return { ok: false, error: err.message };
  }
}

/**
 * Fetches all courses available in the catalog.
 * @param {AbortSignal} [signal] Optional abort signal to cancel pending requests.
 * @returns {Promise<Array<object>>} List of course objects.
 */
export async function fetchCourses(signal) {
  const baseUrl = getApiBaseUrl();
  const res = await fetch(`${baseUrl}${API_ENDPOINTS.COURSES}`, { signal });

  if (!res.ok) {
    throw new Error(`Failed to fetch courses: ${res.status} ${res.statusText}`);
  }

  const json = await res.json();
  return Array.isArray(json.data) ? json.data : [];
}
