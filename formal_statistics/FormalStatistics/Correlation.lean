/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Kutner §2.9, §2.11 — The Correlation Coefficient

The sample correlation coefficient is `r = Sxy/√(Sxx·Syy)`.  We prove
Cauchy–Schwarz `Sxy² ≤ Sxx·Syy`, hence `|r| ≤ 1`, and that `r²` equals the
coefficient of determination `R²`.
-/
import FormalStatistics.GoodnessOfFit

namespace FormalStatistics

variable {n : ℕ}

/-- Sample correlation coefficient. -/
noncomputable def corr (x y : Fin n → ℝ) : ℝ :=
  Sxy x y / Real.sqrt (Sxx x * Syy y)

/-- **Cauchy–Schwarz** for the centered variables: `Sxy² ≤ Sxx·Syy`. -/
theorem Sxy_sq_le (x y : Fin n → ℝ) : Sxy x y ^ 2 ≤ Sxx x * Syy y := by
  have h := Finset.sum_mul_sq_le_sq_mul_sq (Finset.univ)
    (fun i => x i - mean x) (fun i => y i - mean y)
  simpa [Sxy, Sxx, Syy] using h

/-- The correlation coefficient satisfies `|r| ≤ 1` (for non-degenerate data). -/
theorem abs_corr_le_one (x y : Fin n → ℝ) (hSxx : 0 < Sxx x) (hSyy : 0 < Syy y) :
    |corr x y| ≤ 1 := by
  have hden : 0 < Sxx x * Syy y := mul_pos hSxx hSyy
  have hsq : corr x y ^ 2 ≤ 1 := by
    have hcs := Sxy_sq_le x y
    have hs : Real.sqrt (Sxx x * Syy y) ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr hden)
    have hs2 : Real.sqrt (Sxx x * Syy y) ^ 2 = Sxx x * Syy y := Real.sq_sqrt (le_of_lt hden)
    unfold corr
    rw [div_pow, hs2, div_le_one hden]
    linarith
  calc |corr x y| = Real.sqrt (corr x y ^ 2) := (Real.sqrt_sq_eq_abs _).symm
    _ ≤ 1 := Real.sqrt_le_one.mpr hsq

/-- `r² = R²`. -/
theorem corr_sq_eq_R2 (x y : Fin n → ℝ) (hSxx : 0 < Sxx x) (hSyy : 0 < Syy y) :
    corr x y ^ 2 = R2 x y := by
  have hden : 0 < Sxx x * Syy y := mul_pos hSxx hSyy
  have hs : Real.sqrt (Sxx x * Syy y) ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr hden)
  have hs2 : Real.sqrt (Sxx x * Syy y) ^ 2 = Sxx x * Syy y := Real.sq_sqrt (le_of_lt hden)
  unfold corr R2
  rw [div_pow, hs2, SSR_eq]
  unfold b1
  rw [show SSTO y = Syy y from rfl]
  field_simp [ne_of_gt hSxx, ne_of_gt hSyy]
  ring

end FormalStatistics
