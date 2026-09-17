/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Holonomic Constraints and Lagrange Multipliers

A holonomic constraint is a configuration condition `g(q) = 0`, a level set in
configuration space.  Retaining redundant coordinates reintroduces constraint
forces through Lagrange multipliers; eliminating them recovers the unconstrained
Euler–Lagrange equations.  We formalize both the constrained equations and the
reduction when the multipliers vanish.
-/
import Mathlib
import FormalPhysics.Variations.SeveralVariables

namespace FormalPhysics.Lagrangian

open FormalPhysics

/-- A holonomic constraint is the level set `{q | g q = 0}`. -/
def HolonomicConstraint {n : ℕ} (g : (Fin n → ℝ) → ℝ) : Set (Fin n → ℝ) :=
  {q | g q = 0}

/-- The constrained Euler–Lagrange system with `n` multipliers, one per
coordinate: the unconstrained equation plus `Σⱼ λⱼ ∂gⱼ/∂qᵢ`. -/
noncomputable def IsConstrainedEL {n : ℕ} (L : LagrangianFamily n)
    (g : Fin n → (Fin n → ℝ) → ℝ) (lam : Fin n → ℝ) (γ : Fin n → ℝ → ℝ) : Prop :=
  ∀ t i, deriv (fun s => momentum (L i) s (γ i s) (deriv (γ i) s)) t
      = gradX (L i) t (γ i t) (deriv (γ i) t)
        + lam i * fderiv ℝ (g i) (fun j => γ j t) (Pi.single i (1 : ℝ))

/-- **Reduction to the unconstrained system**: when all multipliers vanish the
constrained equations are exactly the unconstrained Euler–Lagrange system. -/
theorem constrainedEL_iff_isELFamily_of_multipliers_zero {n : ℕ} (L : LagrangianFamily n)
    (g : Fin n → (Fin n → ℝ) → ℝ) (lam : Fin n → ℝ) (γ : Fin n → ℝ → ℝ)
    (hlam : ∀ i, lam i = 0) :
    IsConstrainedEL L g lam γ ↔ IsELFamily L γ := by
  unfold IsConstrainedEL IsELFamily IsEL
  constructor
  · intro h i t
    have := h t i
    rw [hlam i, zero_mul, add_zero] at this
    exact this
  · intro h t i
    have := h i t
    rw [hlam i, zero_mul, add_zero]
    exact this

end FormalPhysics.Lagrangian
