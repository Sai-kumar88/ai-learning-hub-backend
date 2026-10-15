import React from "react";
import { Sparkles } from "lucide-react";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="nav-container">
        {/* Brand */}
        <div className="brand">
          <div className="brand-icon-wrapper">
            <Sparkles size={22} color="#ffffff" />
          </div>
          <div>
            <div className="brand-title">AI Course Catalog</div>
            <div className="brand-subtitle">Curated Artificial Intelligence Learning Directory</div>
          </div>
        </div>
      </div>
    </header>
  );
}
