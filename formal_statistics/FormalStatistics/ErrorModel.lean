/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Kutner §1.3, §2.1 — The Additive Error Model

The simple linear regression model writes the response as
`Yᵢ = β₀ + β₁ xᵢ + εᵢ`.  Substituting the model into the least-squares formulas
expresses every estimator as an affine function of the errors — the algebraic
form on which unbiasedness and the variance formulas of Chapter 2 rest:

`b₁ - β₁ = Σ cᵢ εᵢ`,  `cᵢ = (xᵢ - x̄)/Sxx`.
-/
import FormalStatistics.GoodnessOfFit

namespace FormalStatistics

variable {n : ℕ}

/-- Slope coefficient vector `cᵢ = (xᵢ - x̄)/Sxx`. -/
noncomputable def cvec (x : Fin n → ℝ) (i : Fin n) : ℝ := (x i - mean x) / Sxx x

/-- The response mean under the additive error model. -/
theorem mean_expand (x y e : Fin n → ℝ) (b0v b1v : ℝ)
    (hy : ∀ i, y i = b0v + b1v * x i + e i) (hn : (n : ℝ) ≠ 0) :
    mean y = b0v + b1v * mean x + mean e := by
  have hsum : ∑ i, y i = (n : ℝ) * b0v + b1v * (∑ i, x i) + ∑ i, e i := by
    simp_rw [hy, Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ,
      Fintype.card_fin, nsmul_eq_mul]
    rw [← Finset.mul_sum]
    try ring
  unfold mean
  rw [hsum]
  field_simp
  try ring

/-- The corrected cross-product under the additive error model. -/
theorem Sxy_expand (x y e : Fin n → ℝ) (b0v b1v : ℝ)
    (hy : ∀ i, y i = b0v + b1v * x i + e i) (hn : (n : ℝ) ≠ 0) :
    Sxy x y = b1v * Sxx x + Sxy x e := by
  have hycent : ∀ i, y i - mean y = b1v * (x i - mean x) + (e i - mean e) := by
    intro i
    rw [hy i, mean_expand x y e b0v b1v hy hn]
    ring
  have hexp : ∀ i, (x i - mean x) * (b1v * (x i - mean x) + (e i - mean e))
      = b1v * (x i - mean x) ^ 2 + (x i - mean x) * (e i - mean e) := by
    intro i; ring
  unfold Sxy
  simp_rw [hycent, hexp, Finset.sum_add_distrib, ← Finset.mul_sum]
  rfl

/-- **Sampling representation of the slope**: `b₁ - β₁ = Sxy(x, ε)/Sxx`. -/
theorem b1_sub_eq (x y e : Fin n → ℝ) (b0v b1v : ℝ)
    (hy : ∀ i, y i = b0v + b1v * x i + e i) (hn : (n : ℝ) ≠ 0)
    (hSxx : Sxx x ≠ 0) : b1 x y - b1v = Sxy x e / Sxx x := by
  unfold b1
  rw [Sxy_expand x y e b0v b1v hy hn]
  field_simp [hSxx]
  ring

/-- `Σ (xᵢ - x̄) εᵢ = Sxy(x, ε)`. -/
theorem sum_centered_mul_eq (x e : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) :
    ∑ i, (x i - mean x) * e i = Sxy x e := by
  have h2 : ∑ i, (x i - mean x) * (e i - mean e)
      = ∑ i, (x i - mean x) * e i - mean e * ∑ i, (x i - mean x) := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  unfold Sxy
  rw [h2, sum_sub_mean x hn, mul_zero, sub_zero]

/-- `Σ cᵢ εᵢ = Sxy(x, ε)/Sxx`. -/
theorem sum_cvec_mul (x e : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0) :
    ∑ i, cvec x i * e i = Sxy x e / Sxx x := by
  have h1 : ∑ i, (x i - mean x) * e i = Sxy x e := sum_centered_mul_eq x e hn
  have hpoint : ∀ i, cvec x i * e i = (1 / Sxx x) * ((x i - mean x) * e i) := by
    intro i; unfold cvec; ring
  simp_rw [hpoint, ← Finset.mul_sum, h1]
  field_simp [hSxx]
  try ring

/-- **Gauss–Markov form**: the slope error is a linear combination of the model
errors with the fixed coefficients `cᵢ`. -/
theorem b1_sub_eq_cvec (x y e : Fin n → ℝ) (b0v b1v : ℝ)
    (hy : ∀ i, y i = b0v + b1v * x i + e i) (hn : (n : ℝ) ≠ 0)
    (hSxx : Sxx x ≠ 0) : b1 x y - b1v = ∑ i, cvec x i * e i := by
  rw [b1_sub_eq x y e b0v b1v hy hn hSxx, sum_cvec_mul x e hn hSxx]

/-- **Sampling representation of the intercept**. -/
theorem b0_sub_eq (x y e : Fin n → ℝ) (b0v b1v : ℝ)
    (hy : ∀ i, y i = b0v + b1v * x i + e i) (hn : (n : ℝ) ≠ 0)
    (hSxx : Sxx x ≠ 0) :
    b0 x y - b0v = mean e - (Sxy x e / Sxx x) * mean x := by
  have hmean := mean_expand x y e b0v b1v hy hn
  have hb1 : b1 x y = b1v + Sxy x e / Sxx x := by
    have := b1_sub_eq x y e b0v b1v hy hn hSxx
    linarith
  unfold b0
  rw [hmean, hb1]
  ring

end FormalStatistics
