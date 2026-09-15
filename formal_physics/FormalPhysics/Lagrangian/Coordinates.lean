/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Taylor §7.2 — Kinetic Energy in Curvilinear Coordinates

The chain rule gives the velocity in polar, cylindrical and spherical
coordinates; the kinetic energy is a quadratic form with the metric
`v² = Σᵢ hᵢ² q̇ᵢ²`.  For a moving (rheonomic) support the kinetic energy splits
as `T = T₂ + T₁ + T₀`, the origin of the "fictitious" couplings.
-/
import Mathlib

namespace FormalPhysics.Lagrangian

/-- Squared speed in polar coordinates, `ṙ² + r²θ̇²`. -/
noncomputable def v2polar (r dr dθ : ℝ) : ℝ := dr ^ 2 + r ^ 2 * dθ ^ 2

/-- Squared speed in cylindrical coordinates, `ρ̇² + ρ²φ̇² + ż²`. -/
noncomputable def v2cylindrical (rho drho dphi dz : ℝ) : ℝ :=
  drho ^ 2 + rho ^ 2 * dphi ^ 2 + dz ^ 2

/-- Squared speed in spherical coordinates, `ṙ² + r²θ̇² + r²sin²θ φ̇²`. -/
noncomputable def v2spherical (r dr θ dθ dphi : ℝ) : ℝ :=
  dr ^ 2 + r ^ 2 * dθ ^ 2 + r ^ 2 * (Real.sin θ) ^ 2 * dphi ^ 2

/-- Kinetic energy in polar coordinates. -/
noncomputable def Tpolar (m r dr dθ : ℝ) : ℝ := (m / 2) * v2polar r dr dθ

/-- Kinetic energy in cylindrical coordinates. -/
noncomputable def Tcylindrical (m rho drho dphi dz : ℝ) : ℝ :=
  (m / 2) * v2cylindrical rho drho dphi dz

/-- Kinetic energy in spherical coordinates. -/
noncomputable def Tspherical (m r dr θ dθ dphi : ℝ) : ℝ :=
  (m / 2) * v2spherical r dr θ dθ dphi

/-- The squared speed is nonnegative in polar coordinates. -/
theorem v2polar_nonneg (r dr dθ : ℝ) : 0 ≤ v2polar r dr dθ := by
  unfold v2polar; positivity

/-- The squared speed is nonnegative in cylindrical coordinates. -/
theorem v2cylindrical_nonneg (rho drho dphi dz : ℝ) : 0 ≤ v2cylindrical rho drho dphi dz := by
  unfold v2cylindrical; positivity

/-- The squared speed is nonnegative in spherical coordinates. -/
theorem v2spherical_nonneg (r dr θ dθ dphi : ℝ) : 0 ≤ v2spherical r dr θ dθ dphi := by
  unfold v2spherical; positivity

/-- Positive-mass kinetic energy is nonnegative. -/
theorem Tpolar_nonneg (m r dr dθ : ℝ) (hm : 0 ≤ m) : 0 ≤ Tpolar m r dr dθ := by
  unfold Tpolar
  exact mul_nonneg (by linarith) (v2polar_nonneg r dr dθ)

/-- Kinetic energy of a pendulum carried by a support moving as `X(t)`,
`T = ½m[(Ẋ + Lθ̇cosθ)² + (Lθ̇sinθ)²]`. -/
noncomputable def Trheonomic (m L Xdot thdot th : ℝ) : ℝ :=
  (m / 2) * ((Xdot + L * thdot * Real.cos th) ^ 2 + (L * thdot * Real.sin th) ^ 2)

/-- **Rheonomic decomposition** `T = T₂ + T₁ + T₀`: moving the support produces a
cross term `T₁` and a constant term `T₀`, absent for natural coordinates. -/
theorem Trheonomic_decomp (m L Xdot thdot th : ℝ) :
    Trheonomic m L Xdot thdot th
      = (m * L ^ 2 / 2) * thdot ^ 2 + m * L * Xdot * thdot * Real.cos th
        + (m / 2) * Xdot ^ 2 := by
  unfold Trheonomic
  linear_combination (m * L ^ 2 * thdot ^ 2 / 2) * Real.sin_sq_add_cos_sq th

end FormalPhysics.Lagrangian
