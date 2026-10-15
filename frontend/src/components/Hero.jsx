import React from "react";
import { Sparkles } from "lucide-react";

/**
 * Hero presentation section for the course catalog.
 */
export default function Hero() {
  return (
    <section className="hero-section">
      <div className="hero-header">
        <div className="hero-pill">
          <Sparkles size={14} />
          <span>Curated AI Learning Directory</span>
        </div>
        <h1 className="hero-title">
          Empower Your Skills with <span>Artificial Intelligence</span>
        </h1>
        <p className="hero-subtitle">
          Browse world-class, accredited AI courses and tutorials from top research institutions and AI pioneers.
        </p>
      </div>
    </section>
  );
}
