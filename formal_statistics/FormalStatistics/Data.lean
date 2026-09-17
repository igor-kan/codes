/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Data and Sums of Squares

For the simple linear regression model with one predictor, the sample mean and
the corrected sums of squares `Sxx`, `Sxy`, `Syy` are the sufficient statistics
from which every least-squares quantity is built.  This file sets up the data
as functions `Fin n → ℝ` and proves the elementary identities used throughout.
-/
import Mathlib

namespace FormalStatistics

variable {n : ℕ}

/-- Sample mean. -/
noncomputable def mean (z : Fin n → ℝ) : ℝ := (∑ i, z i) / n

/-- Corrected sum of squares of the predictor, `Sxx = Σ (xᵢ - x̄)²`. -/
noncomputable def Sxx (x : Fin n → ℝ) : ℝ := ∑ i, (x i - mean x) ^ 2

/-- Corrected cross-product, `Sxy = Σ (xᵢ - x̄)(yᵢ - ȳ)`. -/
noncomputable def Sxy (x y : Fin n → ℝ) : ℝ :=
  ∑ i, (x i - mean x) * (y i - mean y)

/-- Corrected total sum of squares, `Syy = Σ (yᵢ - ȳ)²`. -/
noncomputable def Syy (y : Fin n → ℝ) : ℝ := ∑ i, (y i - mean y) ^ 2

/-- The deviations from the mean sum to zero. -/
theorem sum_sub_mean (x : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) :
    ∑ i, (x i - mean x) = 0 := by
  have h : ∑ i, (x i - mean x) = (∑ i, x i) - (n : ℝ) * mean x := by
    rw [Finset.sum_sub_distrib]
    simp [Finset.sum_const, nsmul_eq_mul]
  rw [h, mean]
  field_simp
  try ring

/-- `Sxx` is nonnegative. -/
theorem Sxx_nonneg (x : Fin n → ℝ) : 0 ≤ Sxx x := by
  unfold Sxx
  exact Finset.sum_nonneg fun i _ => sq_nonneg _

/-- `Syy` is nonnegative. -/
theorem Syy_nonneg (y : Fin n → ℝ) : 0 ≤ Syy y := by
  unfold Syy
  exact Finset.sum_nonneg fun i _ => sq_nonneg _

/-- `Sxy` is symmetric. -/
theorem Sxy_comm (x y : Fin n → ℝ) : Sxy x y = Sxy y x := by
  unfold Sxy mean
  exact Finset.sum_congr rfl fun i _ => by ring

/-- The computational form of `Sxx`: `Sxx = Σx² - n x̄²`. -/
theorem Sxx_eq (x : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) :
    Sxx x = (∑ i, (x i) ^ 2) - (n : ℝ) * (mean x) ^ 2 := by
  have h : ∀ i, (x i - mean x) ^ 2
      = (x i) ^ 2 - 2 * (mean x) * (x i) + (mean x) ^ 2 := by
    intro i; ring
  unfold Sxx
  simp_rw [h]
  rw [Finset.sum_add_distrib, Finset.sum_sub_distrib]
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  rw [← Finset.mul_sum]
  have hsum : ∑ i, x i = (n : ℝ) * mean x := by
    rw [mean]; field_simp
  rw [hsum]
  ring

end FormalStatistics
