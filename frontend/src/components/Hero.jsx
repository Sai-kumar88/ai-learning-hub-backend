import React from "react";
import { Sparkles } from "lucide-react";

/**
 * Hero presentation section for Vaps Artificial Intelligence Learning Center.
 */
export default function Hero() {
  return (
    <section className="hero-section">
      <div className="hero-header">
        <div className="hero-pill">
          <Sparkles size={14} />
          <span>Curated Learning Directory</span>
        </div>
        <h1 className="hero-title">
          Vaps Artificial Intelligence <span>Learning Center</span>
        </h1>
        <p className="hero-subtitle">
          Explore world-class, accredited AI courses and hands-on curriculums from leading AI pioneers.
        </p>
      </div>
    </section>
  );
}
