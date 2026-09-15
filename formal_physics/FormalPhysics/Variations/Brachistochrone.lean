/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Taylor §6.3 — The Brachistochrone and the Cycloid

The brachistochrone is the curve of fastest descent; its solution is a cycloid.
We formalize the parametric cycloid, its derivatives, and the Beltrami first
integral `y (1 + (dy/dx)²) = 2a` that characterizes it.
-/
import Mathlib
import FormalPhysics.Calculus

namespace FormalPhysics.Variations

open FormalPhysics

/-- Cycloid `x`-coordinate: `a (θ - sin θ)`. -/
noncomputable def cycX (a θ : ℝ) : ℝ := a * (θ - Real.sin θ)

/-- Cycloid `y`-coordinate: `a (1 - cos θ)`. -/
noncomputable def cycY (a θ : ℝ) : ℝ := a * (1 - Real.cos θ)

/-- The derivative of the cycloid's `x`-coordinate. -/
theorem deriv_cycX (a θ : ℝ) :
    deriv (fun θ : ℝ => cycX a θ) θ = a * (1 - Real.cos θ) := by
  have h1 : HasDerivAt (fun θ : ℝ => θ - Real.sin θ) (1 - Real.cos θ) θ :=
    (hasDerivAt_id θ).sub (hasDerivAt_sin θ)
  have h2 := h1.const_mul a
  simpa [cycX] using h2.deriv

/-- The derivative of the cycloid's `y`-coordinate. -/
theorem deriv_cycY (a θ : ℝ) :
    deriv (fun θ : ℝ => cycY a θ) θ = a * Real.sin θ := by
  have h1 : HasDerivAt (fun θ : ℝ => 1 - Real.cos θ) (Real.sin θ) θ := by
    have := (hasDerivAt_const θ (1 : ℝ)).sub (hasDerivAt_cos θ)
    simpa using this
  have h2 := h1.const_mul a
  simpa [cycY] using h2.deriv

/-- The slope of the cycloid, `dy/dx = sin θ / (1 - cos θ)`. -/
noncomputable def cycSlope (θ : ℝ) : ℝ := Real.sin θ / (1 - Real.cos θ)

/-- **Brachistochrone first integral.**  On the cycloid (away from the cusp),
`y (1 + (dy/dx)²) = 2a`, the Beltrami identity in the form `y(1+y'²)=2a`. -/
theorem brachistochrone_first_integral (a θ : ℝ) (h : 1 - Real.cos θ ≠ 0) :
    cycY a θ * (1 + (cycSlope θ) ^ 2) = 2 * a := by
  unfold cycY cycSlope
  field_simp [h]
  linear_combination (a * (1 - Real.cos θ)) * Real.sin_sq_add_cos_sq θ

end FormalPhysics.Variations
