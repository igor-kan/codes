/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Kutner §2.7, §2.9 — Sums of Squares and R²

The total variation of the response splits into the part explained by the
regression and the unexplained error:

`SSTO = SSR + SSE`.

From it we define the coefficient of determination `R² = SSR/SSTO` and prove
`0 ≤ R² ≤ 1`.
-/
import FormalStatistics.LeastSquares

namespace FormalStatistics

variable {n : ℕ}

/-- Total sum of squares, `SSTO = Σ (yᵢ - ȳ)²`. -/
noncomputable def SSTO (y : Fin n → ℝ) : ℝ := Syy y

/-- Regression sum of squares, `SSR = Σ (ŷᵢ - ȳ)²`. -/
noncomputable def SSR (x y : Fin n → ℝ) : ℝ := ∑ i, (fitted x y i - mean y) ^ 2

/-- The fitted line minus the response mean is the slope times the centered
predictor. -/
theorem fitted_sub_mean (x y : Fin n → ℝ) (i : Fin n) :
    fitted x y i - mean y = b1 x y * (x i - mean x) := by
  unfold fitted b0; ring

/-- `SSR = b₁² Sxx`. -/
theorem SSR_eq (x y : Fin n → ℝ) : SSR x y = b1 x y ^ 2 * Sxx x := by
  have h : ∀ i, (fitted x y i - mean y) ^ 2 = b1 x y ^ 2 * (x i - mean x) ^ 2 := by
    intro i; rw [fitted_sub_mean]; ring
  unfold SSR
  simp_rw [h, ← Finset.mul_sum]
  rfl

/-- The cross term in `SSTO = SSE + 2·cross + SSR` vanishes. -/
theorem cross_eq_zero (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0) :
    ∑ i, residual x y i * (b1 x y * (x i - mean x)) = 0 := by
  have h : ∑ i, residual x y i * (b1 x y * (x i - mean x))
      = b1 x y * (∑ i, x i * residual x y i)
        - b1 x y * mean x * (∑ i, residual x y i) := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  rw [h, residual_orthogonal' x y hn hSxx, residual_sum' x y hn]
  ring

/-- **The sum-of-squares decomposition** `SSTO = SSR + SSE`. -/
theorem SSTO_eq_SSR_add_SSE (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0) :
    SSTO y = SSR x y + SSE x y := by
  have h : ∀ i, (y i - mean y) ^ 2
      = (residual x y i) ^ 2 + 2 * (residual x y i * (fitted x y i - mean y))
        + (fitted x y i - mean y) ^ 2 := by
    intro i
    have hy : y i - mean y = residual x y i + (fitted x y i - mean y) := by
      unfold residual fitted; ring
    rw [hy]; ring
  have hcross : ∑ i, 2 * (residual x y i * (fitted x y i - mean y)) = 0 := by
    rw [← Finset.mul_sum]
    have h0 : ∑ i, residual x y i * (fitted x y i - mean y) = 0 := by
      simp_rw [fitted_sub_mean x y]
      exact cross_eq_zero x y hn hSxx
    rw [h0, mul_zero]
  unfold SSTO Syy SSR SSE
  simp_rw [h, Finset.sum_add_distrib, hcross]
  try ring

/-- Coefficient of determination `R² = SSR/SSTO`. -/
noncomputable def R2 (x y : Fin n → ℝ) : ℝ := SSR x y / SSTO y

/-- `R² = 1 - SSE/SSTO`. -/
theorem R2_eq_one_sub (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0)
    (hSSTO : SSTO y ≠ 0) : R2 x y = 1 - SSE x y / SSTO y := by
  have hdecomp := SSTO_eq_SSR_add_SSE x y hn hSxx
  have hne : SSR x y + SSE x y ≠ 0 := by rw [← hdecomp]; exact hSSTO
  unfold R2
  rw [hdecomp]
  field_simp [hne]
  try ring

/-- `R²` is nonnegative. -/
theorem R2_nonneg (x y : Fin n → ℝ) (hSSTO : 0 < SSTO y) : 0 ≤ R2 x y := by
  unfold R2 SSTO Syy
  exact div_nonneg (Finset.sum_nonneg fun i _ => sq_nonneg _)
    (le_of_lt hSSTO)

/-- `R²` never exceeds one. -/
theorem R2_le_one (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0)
    (hSSTO : 0 < SSTO y) : R2 x y ≤ 1 := by
  have hdecomp := SSTO_eq_SSR_add_SSE x y hn hSxx
  have hSSE : 0 ≤ SSE x y := Finset.sum_nonneg fun i _ => sq_nonneg _
  have hSSTO' : 0 < SSTO y := hSSTO
  unfold R2
  rw [div_le_one hSSTO']
  linarith [hdecomp, hSSE]

end FormalStatistics
