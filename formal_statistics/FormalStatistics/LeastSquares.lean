/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Kutner §1.6 — The Least-Squares Criterion

The least-squares criterion is `Q(β₀, β₁) = Σ (yᵢ - β₀ - β₁ xᵢ)²`.  We prove
the **master decomposition**

`Q(β₀, β₁) = SSE + n (β₀ + β₁ x̄ - ȳ)² + Sxx (β₁ - b₁)²`,

which exhibits `(b₀, b₁)` as the unique minimizer for a non-constant predictor,
and gives the minimum value `Q(b₀, b₁) = SSE`.
-/
import FormalStatistics.NormalEquations

namespace FormalStatistics

variable {n : ℕ}

/-- The least-squares criterion. -/
noncomputable def Q (x y : Fin n → ℝ) (β0 β1 : ℝ) : ℝ :=
  ∑ i, (y i - β0 - β1 * x i) ^ 2

/-- Fitted value at observation `i`. -/
noncomputable def fitted (x y : Fin n → ℝ) (i : Fin n) : ℝ := b0 x y + b1 x y * x i

/-- Residual at observation `i`, `eᵢ = yᵢ - ŷᵢ`. -/
noncomputable def residual (x y : Fin n → ℝ) (i : Fin n) : ℝ :=
  y i - b0 x y - b1 x y * x i

/-- Error sum of squares, `SSE = Σ eᵢ²`. -/
noncomputable def SSE (x y : Fin n → ℝ) : ℝ := ∑ i, (residual x y i) ^ 2

/-- The fitted line passes through `(x̄, ȳ)`. -/
theorem b0_add_b1_mul_mean (x y : Fin n → ℝ) :
    b0 x y + b1 x y * mean x = mean y := by
  unfold b0; ring

/-- Recentering a sum of squares of an affine function of the predictor:
`Σ (c + d xᵢ)² = n (c + d x̄)² + d² Sxx`. -/
theorem sum_sq_affine (x : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (c d : ℝ) :
    ∑ i, (c + d * x i) ^ 2 = (n : ℝ) * (c + d * mean x) ^ 2 + Sxx x * d ^ 2 := by
  have h : ∀ i, (c + d * x i) ^ 2
      = ((c + d * mean x) + d * (x i - mean x)) ^ 2 := by
    intro i; ring
  have hexp : ∀ i, ((c + d * mean x) + d * (x i - mean x)) ^ 2
      = (c + d * mean x) ^ 2 + 2 * (c + d * mean x) * d * (x i - mean x)
        + d ^ 2 * (x i - mean x) ^ 2 := by
    intro i; ring
  simp_rw [h, hexp]
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib]
  have h1 : ∑ _i : Fin n, (c + d * mean x) ^ 2 = (n : ℝ) * (c + d * mean x) ^ 2 := by
    simp [Finset.sum_const, nsmul_eq_mul]
  have h2 : ∑ i, 2 * (c + d * mean x) * d * (x i - mean x) = 0 := by
    rw [← Finset.mul_sum, sum_sub_mean x hn, mul_zero]
  have h3 : ∑ i, d ^ 2 * (x i - mean x) ^ 2 = d ^ 2 * Sxx x := by
    rw [← Finset.mul_sum]
    rfl
  rw [h1, h2, h3, add_zero]
  ring

/-- The residuals sum to zero, in terms of the `residual` function. -/
theorem residual_sum' (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) :
    ∑ i, residual x y i = 0 := by
  unfold residual
  exact residual_sum x y hn

/-- The residuals are orthogonal to the predictor, in terms of `residual`. -/
theorem residual_orthogonal' (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0) :
    ∑ i, x i * residual x y i = 0 := by
  unfold residual
  exact residual_orthogonal x y hn hSxx

/-- The criterion splits as `SSE` plus a perfect square in the parameters. -/
theorem Q_eq_SSE_add_sq (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0)
    (β0 β1 : ℝ) :
    Q x y β0 β1 = SSE x y + ∑ i, ((b0 x y - β0) + (b1 x y - β1) * x i) ^ 2 := by
  have hpoint : ∀ i, y i - β0 - β1 * x i
      = residual x y i + ((b0 x y - β0) + (b1 x y - β1) * x i) := by
    intro i; unfold residual; ring
  have hexp : ∀ i, (residual x y i + ((b0 x y - β0) + (b1 x y - β1) * x i)) ^ 2
      = (residual x y i) ^ 2
        + 2 * residual x y i * ((b0 x y - β0) + (b1 x y - β1) * x i)
        + ((b0 x y - β0) + (b1 x y - β1) * x i) ^ 2 := by
    intro i; ring
  have hsplit : ∑ i, 2 * residual x y i * ((b0 x y - β0) + (b1 x y - β1) * x i)
      = ∑ i, (2 * (b0 x y - β0) * residual x y i
              + 2 * (b1 x y - β1) * (x i * residual x y i)) := by
    exact Finset.sum_congr rfl fun i _ => by ring
  have hcross : ∑ i, 2 * residual x y i * ((b0 x y - β0) + (b1 x y - β1) * x i) = 0 := by
    rw [hsplit, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum,
      residual_sum' x y hn, residual_orthogonal' x y hn hSxx, mul_zero, mul_zero, add_zero]
  unfold Q SSE
  simp_rw [hpoint, hexp, Finset.sum_add_distrib]
  rw [hcross]
  ring

/-- The master decomposition of the least-squares criterion. -/
theorem Q_decomposition (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0)
    (β0 β1 : ℝ) :
    Q x y β0 β1
      = SSE x y + (n : ℝ) * (β0 + β1 * mean x - mean y) ^ 2
        + Sxx x * (β1 - b1 x y) ^ 2 := by
  rw [Q_eq_SSE_add_sq x y hn hSxx β0 β1]
  have h := sum_sq_affine x hn (b0 x y - β0) (b1 x y - β1)
  rw [h]
  have hc : (b0 x y - β0) + (b1 x y - β1) * mean x
      = -(β0 + β1 * mean x - mean y) := by
    have := b0_add_b1_mul_mean x y
    linarith
  rw [hc]
  ring

/-- The least-squares estimates achieve the error sum of squares. -/
theorem Q_b0_b1 (x y : Fin n → ℝ) : Q x y (b0 x y) (b1 x y) = SSE x y := by
  unfold Q SSE residual
  rfl

/-- **The least-squares estimates are a global minimizer** of `Q`. -/
theorem SSE_le_Q (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0)
    (β0 β1 : ℝ) : SSE x y ≤ Q x y β0 β1 := by
  rw [Q_decomposition x y hn hSxx β0 β1]
  have h1 : 0 ≤ (n : ℝ) * (β0 + β1 * mean x - mean y) ^ 2 :=
    mul_nonneg (Nat.cast_nonneg n) (sq_nonneg _)
  have h2 : 0 ≤ Sxx x * (β1 - b1 x y) ^ 2 := mul_nonneg (Sxx_nonneg x) (sq_nonneg _)
  linarith

/-- `(b₀, b₁)` minimizes `Q`. -/
theorem isMinOn_Q (x y : Fin n → ℝ) (hn : (n : ℝ) ≠ 0) (hSxx : Sxx x ≠ 0)
    (β0 β1 : ℝ) : Q x y (b0 x y) (b1 x y) ≤ Q x y β0 β1 := by
  rw [Q_b0_b1]
  exact SSE_le_Q x y hn hSxx β0 β1

/-- For a non-constant predictor the least-squares minimizer is **unique**. -/
theorem Q_eq_SSE_iff (x y : Fin n → ℝ) (hn : 0 < (n : ℝ)) (hSxx : 0 < Sxx x)
    (β0 β1 : ℝ) : Q x y β0 β1 = SSE x y ↔ β0 = b0 x y ∧ β1 = b1 x y := by
  rw [Q_decomposition x y (ne_of_gt hn) (ne_of_gt hSxx) β0 β1]
  constructor
  · intro h
    have h1 : 0 ≤ (n : ℝ) * (β0 + β1 * mean x - mean y) ^ 2 :=
      mul_nonneg (le_of_lt hn) (sq_nonneg _)
    have h2 : 0 ≤ Sxx x * (β1 - b1 x y) ^ 2 := mul_nonneg (le_of_lt hSxx) (sq_nonneg _)
    have h3 : (n : ℝ) * (β0 + β1 * mean x - mean y) ^ 2 = 0 := by linarith
    have h4 : Sxx x * (β1 - b1 x y) ^ 2 = 0 := by linarith
    have hL : β0 + β1 * mean x - mean y = 0 := by
      rcases mul_eq_zero.mp h3 with h | h
      · exact absurd h (ne_of_gt hn)
      · exact sq_eq_zero_iff.mp h
    have hd : β1 - b1 x y = 0 := by
      rcases mul_eq_zero.mp h4 with h | h
      · exact absurd h (ne_of_gt hSxx)
      · exact sq_eq_zero_iff.mp h
    have hb1 : β1 = b1 x y := by linarith
    have hb0 : β0 = b0 x y := by
      have := b0_add_b1_mul_mean x y
      rw [hb1] at hL
      linarith
    exact ⟨hb0, hb1⟩
  · rintro ⟨rfl, rfl⟩
    have hL : b0 x y + b1 x y * mean x = mean y := b0_add_b1_mul_mean x y
    rw [hL]
    ring

end FormalStatistics
