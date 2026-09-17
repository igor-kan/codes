/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Inference, ANOVA and the F = t² Identity

This file defines the standard inference quantities — the error mean square
`MSE`, the standard error of the slope, the `t` statistic, the ANOVA mean square
`MSR` and the `F` statistic — and proves the canonical identity `F = t²`.
-/
import FormalStatistics.GoodnessOfFit

namespace FormalStatistics

variable {n : ℕ}

/-- Error mean square `MSE = SSE/(n - 2)`. -/
noncomputable def MSE (x y : Fin n → ℝ) : ℝ := SSE x y / ((n : ℝ) - 2)

/-- Regression mean square `MSR = SSR/1`. -/
noncomputable def MSR (x y : Fin n → ℝ) : ℝ := SSR x y

/-- Estimated standard error of the slope, `s{b₁} = √(MSE/Sxx)`. -/
noncomputable def seB1 (x y : Fin n → ℝ) : ℝ := Real.sqrt (MSE x y / Sxx x)

/-- The `t` statistic for `H₀ : β₁ = 0`, `t = b₁/s{b₁}`. -/
noncomputable def tStat (x y : Fin n → ℝ) : ℝ := b1 x y / seB1 x y

/-- The ANOVA `F` statistic, `F = MSR/MSE`. -/
noncomputable def FStat (x y : Fin n → ℝ) : ℝ := MSR x y / MSE x y

/-- `s{b₁}² = MSE/Sxx`. -/
theorem seB1_sq (x y : Fin n → ℝ) (h : 0 ≤ MSE x y / Sxx x) :
    seB1 x y ^ 2 = MSE x y / Sxx x := by
  unfold seB1
  exact Real.sq_sqrt h

/-- **`F = t²`**: the ANOVA `F` statistic for the slope equals the square of
its `t` statistic. -/
theorem FStat_eq_tStat_sq (x y : Fin n → ℝ) (hSxx : 0 < Sxx x)
    (hMSE : 0 < MSE x y) : FStat x y = tStat x y ^ 2 := by
  have hratio : 0 < MSE x y / Sxx x := div_pos hMSE hSxx
  have hsq : seB1 x y ^ 2 = MSE x y / Sxx x := seB1_sq x y (le_of_lt hratio)
  unfold FStat MSR tStat
  rw [SSR_eq, div_pow, hsq]
  field_simp [ne_of_gt hMSE, ne_of_gt hSxx]
  try ring

/-- Standard error of the estimated mean response at `x = h`. -/
noncomputable def seMean (x y : Fin n → ℝ) (h : ℝ) : ℝ :=
  Real.sqrt (MSE x y * (1 / n + (h - mean x) ^ 2 / Sxx x))

/-- Standard error of a predicted new observation at `x = h`. -/
noncomputable def sePredict (x y : Fin n → ℝ) (h : ℝ) : ℝ :=
  Real.sqrt (MSE x y * (1 + 1 / n + (h - mean x) ^ 2 / Sxx x))

/-- The prediction variance strictly exceeds the mean-response variance: the
extra `MSE` accounts for the new observation's own error. -/
theorem sePredict_sq_eq (x y : Fin n → ℝ) (h : ℝ) (hMSE : 0 ≤ MSE x y)
    (hinner : 0 ≤ 1 + 1 / n + (h - mean x) ^ 2 / Sxx x) :
    sePredict x y h ^ 2
      = MSE x y * (1 + 1 / n + (h - mean x) ^ 2 / Sxx x) := by
  unfold sePredict
  exact Real.sq_sqrt (mul_nonneg hMSE hinner)

end FormalStatistics
