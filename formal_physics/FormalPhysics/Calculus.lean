/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Reusable calculus lemmas for the physics formalization

Small, self-contained facts about `HasDerivAt` used throughout the
formalization.  Keeping them in one place means every later file proves physics,
not derivative bookkeeping.
-/
import Mathlib

namespace FormalPhysics

/-- The derivative of `w ↦ w²` is `2w`. -/
theorem hasDerivAt_sq (x : ℝ) : HasDerivAt (fun w : ℝ => w ^ 2) (2 * x) x := by
  simpa using hasDerivAt_pow 2 x

/-- The derivative of `w ↦ c * w²` is `c * (2w)`. -/
theorem hasDerivAt_sq_const_mul (c x : ℝ) :
    HasDerivAt (fun w : ℝ => c * w ^ 2) (c * (2 * x)) x :=
  (hasDerivAt_sq x).const_mul c

/-- `deriv` of the square function. -/
theorem deriv_sq (x : ℝ) : deriv (fun w : ℝ => w ^ 2) x = 2 * x :=
  (hasDerivAt_sq x).deriv

/-- The derivative of `sin`. -/
theorem hasDerivAt_sin (x : ℝ) : HasDerivAt (fun x : ℝ => Real.sin x) (Real.cos x) x := by
  simpa using (hasDerivAt_id x).sin

/-- The derivative of `cos`. -/
theorem hasDerivAt_cos (x : ℝ) :
    HasDerivAt (fun x : ℝ => Real.cos x) (-Real.sin x) x := by
  simpa using (hasDerivAt_id x).cos

/-- The derivative of a straight line is its slope. -/
theorem deriv_line (m b : ℝ) : deriv (fun x : ℝ => m * x + b) = fun _ => m := by
  funext x
  have h : HasDerivAt (fun x : ℝ => m * x + b) m x := by
    simpa using ((hasDerivAt_id x).const_mul m).add_const b
  exact h.deriv

/-- The second derivative of a straight line vanishes. -/
theorem deriv_deriv_line (m b : ℝ) :
    deriv (deriv (fun x : ℝ => m * x + b)) = fun _ => 0 := by
  rw [deriv_line]
  funext x
  exact deriv_const x m

/-- The derivative of the identity is `1`. -/
theorem deriv_id_eq (x : ℝ) : deriv (fun x : ℝ => x) x = 1 :=
  (hasDerivAt_id x).deriv

/-- The derivative of a constant function is `0`. -/
theorem deriv_const_eq (c x : ℝ) : deriv (fun _ : ℝ => c) x = 0 :=
  deriv_const x c

end FormalPhysics
