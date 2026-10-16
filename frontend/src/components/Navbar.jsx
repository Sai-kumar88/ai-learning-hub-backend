import React from "react";
import vapsLogo from "../assets/vaps_logo.png";

/**
 * Top navigation header featuring official VAPS logo and organization branding.
 */
export default function Navbar() {
  return (
    <header className="navbar">
      <div className="nav-container">
        {/* Brand with Left-aligned Company Logo */}
        <div className="brand">
          <img 
            src={vapsLogo} 
            alt="VAPS Technosoft Logo" 
            className="brand-logo-img" 
          />
          <div className="brand-divider" aria-hidden="true" />
          <div className="brand-text-group">
            <div className="brand-title">Vaps Artificial Intelligence Learning Center</div>
          </div>
        </div>
      </div>
    </header>
  );
}
