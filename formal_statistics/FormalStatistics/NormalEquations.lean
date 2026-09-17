/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Least-Squares Estimators and the Normal Equations

The least-squares estimates are `b₁ = Sxy/Sxx` and `b₀ = ȳ - b₁ x̄`.  This file
proves that the corresponding residuals satisfy the two **normal equations**
`Σ eᵢ = 0` and `Σ xᵢ eᵢ = 0`, which are the algebraic engine behind every later
result (the sum-of-squares decomposition, `R²`, and the sampling properties).
-/
import FormalStatistics.Data

namespace FormalStatistics

variable {n : ℕ}

/-- Least-squares slope `b₁ = Sxy / Sxx`. -/
noncomputable def b1 (x y : Fin n → ℝ) : ℝ := Sxy x y / Sxx x

/-- Least-squares intercept `b₀ = ȳ - b₁ x̄`. -/
noncomputable def b0 (x y : Fin n → ℝ) : ℝ := mean y - b1 x y * mean x

/-- `Σ xᵢ (yᵢ - ȳ) = Sxy`. -/
theorem sum_mul_centered (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) :
    ∑ i, x i * (y i - mean y) = Sxy x y := by
  have h1 : ∑ i, x i * (y i - mean y) - ∑ i, mean x * (y i - mean y)
      = ∑ i, (x i - mean x) * (y i - mean y) := by
    rw [← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  have h2 : ∑ i, mean x * (y i - mean y) = 0 := by
    rw [← Finset.mul_sum, sum_sub_mean y hn, mul_zero]
  unfold Sxy
  linarith

/-- `Σ xᵢ (xᵢ - x̄) = Sxx`. -/
theorem sum_mul_self_centered (x : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) :
    ∑ i, x i * (x i - mean x) = Sxx x := by
  have h1 : ∑ i, x i * (x i - mean x)
      = ∑ i, (x i - mean x) * (x i - mean x) := by
    have h1' : ∑ i, x i * (x i - mean x) - ∑ i, mean x * (x i - mean x)
        = ∑ i, (x i - mean x) * (x i - mean x) := by
      rw [← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun i _ => by ring
    have h2 : ∑ i, mean x * (x i - mean x) = 0 := by
      rw [← Finset.mul_sum, sum_sub_mean x hn, mul_zero]
    linarith
  rw [h1]
  unfold Sxx
  exact Finset.sum_congr rfl fun i _ => by ring

/-- The residual in centered form. -/
theorem residual_eq (x y : Fin n → ℝ) (i : Fin n) :
    y i - b0 x y - b1 x y * x i = (y i - mean y) - b1 x y * (x i - mean x) := by
  unfold b0; ring

/-- **First normal equation**: the residuals sum to zero. -/
theorem residual_sum (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) :
    ∑ i, (y i - b0 x y - b1 x y * x i) = 0 := by
  simp_rw [residual_eq x y]
  rw [Finset.sum_sub_distrib, ← Finset.mul_sum, sum_sub_mean y hn, sum_sub_mean x hn,
    mul_zero, sub_zero]

/-- **Second normal equation**: the residuals are orthogonal to the predictor. -/
theorem residual_orthogonal (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0)
    (hSxx : Sxx x ≠ 0) :
    ∑ i, x i * (y i - b0 x y - b1 x y * x i) = 0 := by
  have hcongr : ∀ i, x i * (y i - b0 x y - b1 x y * x i)
      = x i * (y i - mean y) - b1 x y * (x i * (x i - mean x)) := by
    intro i; unfold b0; ring
  simp_rw [hcongr]
  rw [Finset.sum_sub_distrib, ← Finset.mul_sum, sum_mul_centered x y hn,
    sum_mul_self_centered x hn, b1]
  field_simp [hSxx]
  try ring

end FormalStatistics
