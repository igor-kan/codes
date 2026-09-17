/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Functionals of Several Variables

When the functional depends on `n` independent functions, variation gives one
Euler–Lagrange equation per function.  We formalize the family of equations and
prove it decouples for independent Lagrangians.
-/
import Mathlib
import FormalPhysics.Lagrangian.EulerLagrange

namespace FormalPhysics.Lagrangian

open FormalPhysics

/-- A family of `n` independent scalar Lagrangians. -/
abbrev LagrangianFamily (n : ℕ) := Fin n → ScalarLagrangian

/-- The system of Euler–Lagrange equations, one per dependent function. -/
def IsELFamily {n : ℕ} (L : LagrangianFamily n) (γ : Fin n → ℝ → ℝ) : Prop :=
  ∀ i, IsEL (L i) (γ i)

/-- The system predicate is, definitionally, the conjunction of the individual
Euler–Lagrange equations. -/
theorem isELFamily_iff {n : ℕ} (L : LagrangianFamily n) (γ : Fin n → ℝ → ℝ) :
    IsELFamily L γ ↔ ∀ i, IsEL (L i) (γ i) := Iff.rfl

/-- A family of decoupled conservative Lagrangians. -/
noncomputable def freeLagFamily {n : ℕ} (m : Fin n → ℝ) (U : Fin n → ℝ → ℝ) :
    LagrangianFamily n :=
  fun i => freeLag (m i) (U i)

/-- For decoupled conservative systems the Euler–Lagrange system is equivalent
to the individual Newton equations. -/
theorem isELFamily_freeLag_iff {n : ℕ} (m : Fin n → ℝ) (U : Fin n → ℝ → ℝ)
    (γ : Fin n → ℝ → ℝ) (hU : ∀ i x, DifferentiableAt ℝ (U i) x)
    (hγ : ∀ i, Differentiable ℝ (deriv (γ i))) :
    IsELFamily (freeLagFamily m U) γ ↔ ∀ i, IsNewtonian (m i) (U i) (γ i) := by
  unfold IsELFamily freeLagFamily
  constructor
  · intro h i
    exact (isEL_freeLag_iff_newtonian (m i) (U i) (γ i) (hU i) (hγ i)).mp (h i)
  · intro h i
    exact (isEL_freeLag_iff_newtonian (m i) (U i) (γ i) (hU i) (hγ i)).mpr (h i)

end FormalPhysics.Lagrangian
