/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# The Legendre Transform

The Legendre transform trades velocity for momentum: `p = ∂L/∂v`, and the
Hamiltonian is `H = p v - L`.  In one dimension with `L = ½ m v²`, the transform
is an involution on quadratic functions and yields `H = p²/(2m)`.
-/
import Mathlib
import FormalPhysics.Calculus

namespace FormalPhysics.Hamiltonian

open FormalPhysics

/-- The quadratic Lagrangian `L(v) = ½ m v²`. -/
noncomputable def kinetic (m v : ℝ) : ℝ := (m / 2) * v ^ 2

/-- The conjugate momentum `p = dL/dv = m v`. -/
noncomputable def momentum (m v : ℝ) : ℝ := deriv (fun v : ℝ => kinetic m v) v

/-- The conjugate momentum is `m v`. -/
theorem momentum_eq (m v : ℝ) : momentum m v = m * v := by
  unfold momentum kinetic
  have h : HasDerivAt (fun v : ℝ => (m / 2) * v ^ 2) (m * v) v := by
    have := (hasDerivAt_sq v).const_mul (m / 2)
    convert this using 1
    ring
  exact h.deriv

/-- The Legendre transform of `L(v) = ½ m v²` is `H(p) = p²/(2m)`. -/
noncomputable def hamiltonian (m p : ℝ) : ℝ := (1 / (2 * m)) * p ^ 2

/-- **Legendre involution on quadratics**: transforming the momentum back gives
the original Lagrangian, `H(p(v)) = L(v)`. -/
theorem hamiltonian_momentum (m v : ℝ) (hm : m ≠ 0) :
    hamiltonian m (momentum m v) = kinetic m v := by
  rw [momentum_eq]
  unfold hamiltonian kinetic
  field_simp
  ring

/-- The Legendre transform can also be written `H(p) = p v - L(v)` at the
stationary point `p = L'(v)`, here verified directly. -/
theorem hamiltonian_eq_legendre_pair (m v : ℝ) (hm : m ≠ 0) :
    hamiltonian m (momentum m v) = momentum m v * v - kinetic m v := by
  rw [momentum_eq]
  unfold hamiltonian kinetic
  field_simp
  ring

end FormalPhysics.Hamiltonian
