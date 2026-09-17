/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Configuration Space and Generalised Momentum

The configuration space of a free particle in `n` dimensions is the Euclidean
space `EuclideanSpace ℝ (Fin n)`.  A Lagrangian is a scalar on `Q × TQ`, and the
canonical momentum is the gradient `∂L/∂v` — a Fréchet derivative represented by
a vector in Mathlib.
-/
import Mathlib
import FormalPhysics.Lagrangian.EulerLagrange

namespace FormalPhysics.Lagrangian

open FormalPhysics

/-- The configuration space of a free particle in `n` dimensions. -/
abbrev Configuration (n : ℕ) := EuclideanSpace ℝ (Fin n)

/-- Kinetic energy `T = ½ m ‖v‖²`. -/
noncomputable def kinetic {n : ℕ} (m : ℝ) (v : Configuration n) : ℝ :=
  (m / 2) * ‖v‖ ^ 2

/-- Kinetic energy of a positive mass is nonnegative. -/
theorem kinetic_nonneg {n : ℕ} (m : ℝ) (hm : 0 ≤ m) (v : Configuration n) :
    0 ≤ kinetic m v := by
  unfold kinetic
  exact mul_nonneg (by linarith) (by positivity)

/-- The canonical (generalized) momentum as the gradient of the Lagrangian in
the velocity: `p = ∂L/∂v`, a theorem-grade object in the inner-product space
`Q`. -/
noncomputable def generalizedMomentum {n : ℕ}
    (L : Configuration n → Configuration n → ℝ) (x v : Configuration n) : Configuration n :=
  gradient (fun w => L x w) v

/-- Definitional unfolding: the canonical momentum is the gradient of `L` in the
velocity. -/
theorem generalizedMomentum_def {n : ℕ}
    (L : Configuration n → Configuration n → ℝ) (x v : Configuration n) :
    generalizedMomentum L x v = gradient (fun w => L x w) v := rfl

end FormalPhysics.Lagrangian
