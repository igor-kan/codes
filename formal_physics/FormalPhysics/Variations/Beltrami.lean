/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Taylor §6.3 — The Beltrami Identity

When the integrand `f(y, y')` has no explicit dependence on the independent
variable, the Euler–Lagrange equation has the first integral

  `f - y' ∂f/∂y' = const,`

the **Beltrami identity**.  We isolate this identity algebraically and verify it
for the two textbook integrands: the arc length of a plane curve and the
brachistochrone time functional.
-/
import Mathlib

namespace FormalPhysics.Variations

/-- The Beltrami expression `f(y, p) - p · fp(y, p)`. -/
noncomputable def beltrami (f fp : ℝ → ℝ → ℝ) (y p : ℝ) : ℝ := f y p - p * fp y p

/-- Arc-length integrand `√(1 + p²)`. -/
noncomputable def arclengthF (p : ℝ) : ℝ := Real.sqrt (1 + p ^ 2)

/-- Its derivative with respect to the slope, `p / √(1 + p²)`. -/
noncomputable def arclengthFp (p : ℝ) : ℝ := p / Real.sqrt (1 + p ^ 2)

/-- **Beltrami identity for the shortest path**: `f - p f_p = 1/√(1+p²)`,
which is constant along a straight line (where `p` is constant). -/
theorem beltrami_shortest (p : ℝ) :
    beltrami (fun _ => arclengthF) (fun _ => arclengthFp) 0 p
      = 1 / Real.sqrt (1 + p ^ 2) := by
  unfold beltrami arclengthF arclengthFp
  set s := Real.sqrt (1 + p ^ 2) with hs
  have hs2 : s ^ 2 = 1 + p ^ 2 := by
    rw [hs]; exact Real.sq_sqrt (by positivity)
  have hs0 : s ≠ 0 := by
    have : 0 < Real.sqrt (1 + p ^ 2) := Real.sqrt_pos.mpr (by positivity)
    exact ne_of_gt this
  field_simp [hs0]
  nlinarith [hs2]

/-- **Beltrami identity for the brachistochrone**, in the form in which the
first integral is usually written: with `f² = (1+p²)/y`,
`f - p·(p/(y f)) = 1/(y f)`.  This is the algebraic content of
`y(1 + y'²) = 1/C²`. -/
theorem beltrami_brachistochrone (f y p : ℝ) (hy : y ≠ 0) (hf : f ≠ 0)
    (hf2 : f ^ 2 = (1 + p ^ 2) / y) :
    f - p * (p / (y * f)) = 1 / (y * f) := by
  have hf2' : f ^ 2 * y = 1 + p ^ 2 := by
    rw [hf2]
    field_simp [hy]
  field_simp [hy, hf]
  nlinarith [hf2']

end FormalPhysics.Variations
