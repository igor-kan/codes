/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Cyclic Coordinates and Noether's Theorem

If the Lagrangian does not depend on a coordinate `x` (the coordinate is
*cyclic*), then the Euler–Lagrange equation becomes the statement that the
conjugate momentum `p = ∂L/∂v` is conserved.  This is the simplest instance of
Noether's theorem: a symmetry (translation in `x`) gives a conservation law.
-/
import Mathlib
import FormalPhysics.Lagrangian.EulerLagrange

namespace FormalPhysics.Lagrangian

open FormalPhysics

/-- A Lagrangian is *cyclic* in the coordinate `x` if it does not depend on `x`. -/
def IsCyclic (L : ScalarLagrangian) : Prop := ∀ t x x' v, L t x v = L t x' v

/-- For a cyclic Lagrangian the generalized force `∂L/∂x` vanishes. -/
theorem gradX_cyclic (L : ScalarLagrangian) (hL : IsCyclic L) (t x v : ℝ) :
    gradX L t x v = 0 := by
  unfold gradX
  have hfun : (fun y : ℝ => L t y v) = fun _ => L t x v := by
    funext y
    exact hL t y x v
  rw [hfun]
  simp

/-- **Noether's theorem for cyclic coordinates.**  The Euler–Lagrange equation
for a cyclic coordinate is exactly the conservation of the conjugate momentum. -/
theorem isEL_cyclic_iff_momentum_conserved (L : ScalarLagrangian) (γ : ℝ → ℝ)
    (hL : IsCyclic L) :
    IsEL L γ ↔ ∀ t, deriv (fun s => momentum L s (γ s) (deriv γ s)) t = 0 := by
  unfold IsEL
  constructor
  · intro h t
    rw [h t, gradX_cyclic L hL t (γ t) (deriv γ t)]
  · intro h t
    rw [h t, gradX_cyclic L hL t (γ t) (deriv γ t)]

/-- Consequently, a cyclic coordinate yields a conserved quantity. -/
theorem cyclic_momentum_conserved (L : ScalarLagrangian) (γ : ℝ → ℝ)
    (hL : IsCyclic L) (hEL : IsEL L γ) :
    ∀ t, deriv (fun s => momentum L s (γ s) (deriv γ s)) t = 0 :=
  (isEL_cyclic_iff_momentum_conserved L γ hL).mp hEL

end FormalPhysics.Lagrangian
