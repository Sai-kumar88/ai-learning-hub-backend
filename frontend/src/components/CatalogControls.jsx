import React from "react";
import { Search, RotateCw, X } from "lucide-react";

/**
 * Filter and search control bar for the course catalog.
 */
export default function CatalogControls({
  searchQuery,
  onSearchChange,
  selectedProvider,
  onProviderChange,
  providers = [],
  totalCourses = 0,
  filteredCount = 0,
  isLoading = false,
  onRefresh
}) {
  return (
    <>
      <div className="control-bar">
        {/* Search Input Box */}
        <div className="search-box">
          <Search size={16} className="search-icon" aria-hidden="true" />
          <input
            type="text"
            className="search-input"
            placeholder="Search courses by title or provider (e.g. Claude, Anthropic)..."
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
            aria-label="Search courses"
          />
          {searchQuery && (
            <button
              type="button"
              onClick={() => onSearchChange("")}
              style={{
                background: "transparent",
                border: "none",
                cursor: "pointer",
                display: "flex",
                padding: "4px"
              }}
              title="Clear search query"
              aria-label="Clear search"
            >
              <X size={15} color="var(--text-muted)" />
            </button>
          )}
        </div>

        {/* Provider Filter Chips & Refresh Action */}
        <div className="filter-group" role="group" aria-label="Filter by provider">
          <button
            type="button"
            className={`filter-chip ${selectedProvider === "all" ? "active" : ""}`}
            onClick={() => onProviderChange("all")}
          >
            All Providers ({totalCourses})
          </button>

          {providers.map((provider) => (
            <button
              key={provider}
              type="button"
              className={`filter-chip ${selectedProvider === provider ? "active" : ""}`}
              onClick={() => onProviderChange(provider)}
            >
              {provider}
            </button>
          ))}

          <button
            type="button"
            className="btn-secondary"
            onClick={onRefresh}
            disabled={isLoading}
            title="Refresh courses catalog"
            style={{ marginLeft: "0.5rem" }}
            aria-label="Refresh catalog"
          >
            <RotateCw size={14} className={isLoading ? "animate-spin" : ""} />
            <span>Refresh</span>
          </button>
        </div>
      </div>

      {/* Results Count Summary */}
      <div 
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          margin: "1rem 0 1.5rem",
          color: "var(--text-muted)",
          fontSize: "0.875rem",
          fontWeight: 500
        }}
      >
        <span>
          Showing <strong style={{ color: "var(--text-main)" }}>{filteredCount}</strong>{" "}
          {filteredCount === 1 ? "course" : "courses"}
          {selectedProvider !== "all" && ` from ${selectedProvider}`}
          {searchQuery && ` matching "${searchQuery}"`}
        </span>
      </div>
    </>
  );
}
