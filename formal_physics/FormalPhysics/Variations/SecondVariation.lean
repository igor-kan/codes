/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Second Variation, Legendre's Condition, Conjugate Points

The character of a stationary path (minimum, maximum, saddle) is decided by the
second variation.  Legendre's condition is `∂²f/∂y'² > 0`; for the harmonic
oscillator the second variation of the action on a mode `sin(πt/T)` flips sign
at the conjugate time `T = π/ω`, turning a minimum into a saddle.
-/
import Mathlib
import FormalPhysics.Calculus

namespace FormalPhysics.Variations

open FormalPhysics

/-- Legendre's `P = ∂²f/∂v²`, here modelled by differentiating the momentum
`v ↦ m v` of a quadratic kinetic term. -/
noncomputable def legendreP (m : ℝ) (v : ℝ) : ℝ := deriv (fun v : ℝ => m * v) v

/-- Legendre's condition value is the mass `m`, hence positive for `m > 0`. -/
theorem legendreP_eq (m v : ℝ) : legendreP m v = m := by
  unfold legendreP
  have h : HasDerivAt (fun v : ℝ => m * v) m v := by
    simpa using (hasDerivAt_id v).const_mul m
  exact h.deriv

/-- The second variation of the harmonic-oscillator action evaluated on the
mode `η(t) = sin(π t / T)` with fixed endpoints, `(mT/4)((π/T)² - ω²)`. -/
noncomputable def secondVariationHO (m k T : ℝ) : ℝ :=
  (m * T / 4) * ((Real.pi / T) ^ 2 - k / m)

/-- Below the conjugate time the stationary path is a local **minimum**. -/
theorem secondVariationHO_pos (m k T : ℝ) (hm : 0 < m) (hT : 0 < T)
    (h : k / m < (Real.pi / T) ^ 2) : 0 < secondVariationHO m k T := by
  unfold secondVariationHO
  have h1 : 0 < m * T / 4 := by positivity
  have h2 : 0 < (Real.pi / T) ^ 2 - k / m := by linarith
  exact mul_pos h1 h2

/-- Beyond the conjugate time the stationary path is a **saddle**. -/
theorem secondVariationHO_neg (m k T : ℝ) (hm : 0 < m) (hT : 0 < T)
    (h : (Real.pi / T) ^ 2 < k / m) : secondVariationHO m k T < 0 := by
  unfold secondVariationHO
  have h1 : 0 < m * T / 4 := by positivity
  have h2 : (Real.pi / T) ^ 2 - k / m < 0 := by linarith
  exact mul_neg_of_pos_of_neg h1 h2

/-- The conjugate time of the harmonic oscillator, `π/ω` with `ω = √(k/m)`. -/
noncomputable def conjugateTime (m k : ℝ) : ℝ := Real.pi / Real.sqrt (k / m)

/-- At the conjugate time the second variation vanishes: the stationary path
ceases to be a strict minimum. -/
theorem secondVariationHO_at_conjugate (m k : ℝ) (hm : 0 < m) (hk : 0 < k) :
    secondVariationHO m k (conjugateTime m k) = 0 := by
  unfold secondVariationHO conjugateTime
  have hkm : (0 : ℝ) < k / m := by positivity
  have hs : Real.sqrt (k / m) ≠ 0 := by positivity
  have hs2 : (Real.sqrt (k / m)) ^ 2 = k / m := Real.sq_sqrt (le_of_lt hkm)
  have h1 : Real.pi / (Real.pi / Real.sqrt (k / m)) = Real.sqrt (k / m) := by
    field_simp [hs, Real.pi_ne_zero]
    ring
  rw [h1, hs2, sub_self, mul_zero]

end FormalPhysics.Variations
