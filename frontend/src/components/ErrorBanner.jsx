import React from "react";
import { AlertCircle } from "lucide-react";

/**
 * Error display banner with retry button.
 */
export default function ErrorBanner({ message, onRetry }) {
  if (!message) return null;

  return (
    <div 
      role="alert"
      style={{
        background: "#fef2f2",
        border: "1px solid #fecaca",
        borderRadius: "var(--radius-lg)",
        padding: "1.25rem 1.5rem",
        marginBottom: "2rem",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        color: "#991b1b"
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: "0.75rem" }}>
        <AlertCircle size={22} color="#dc2626" />
        <div>
          <strong style={{ color: "#7f1d1d" }}>Backend Connection Issue: </strong>
          <span>{message}</span>
        </div>
      </div>
      <div>
        <button 
          type="button"
          className="btn-primary" 
          onClick={onRetry}
          style={{ fontSize: "0.85rem", padding: "0.45rem 0.9rem" }}
        >
          Retry
        </button>
      </div>
    </div>
  );
}
