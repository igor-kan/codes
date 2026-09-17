/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# The Euler–Lagrange Operator

For a scalar Lagrangian `L(t, x, v)` we define the generalized momentum
`p = ∂L/∂v`, the generalized force `∂L/∂x`, and the Euler–Lagrange predicate
`d/dt (∂L/∂v) = ∂L/∂x`.  The main results show that, for a conservative
Lagrangian `L = T - U` with `T = ½ m v²`, the Euler–Lagrange equation is
*equivalent* to Newton's second law, and that the harmonic oscillator obeys
`m γ'' + k γ = 0`.

Smoothness of the potential is an explicit hypothesis: this is exactly the kind
of silent assumption that Mathlib forces us to name.
-/
import Mathlib

namespace FormalPhysics.Lagrangian

open scoped Topology

/-- A scalar Lagrangian: a function of time, position and velocity. -/
abbrev ScalarLagrangian := ℝ → ℝ → ℝ → ℝ

/-- The generalized momentum `p = ∂L/∂v`. -/
noncomputable def momentum (L : ScalarLagrangian) (t x v : ℝ) : ℝ :=
  deriv (fun w => L t x w) v

/-- The generalized force `∂L/∂x`. -/
noncomputable def gradX (L : ScalarLagrangian) (t x v : ℝ) : ℝ :=
  deriv (fun y => L t y v) x

/-- The Euler–Lagrange equation for a trajectory `γ`:
`d/dt (∂L/∂v) - ∂L/∂x = 0`, written as `d/dt p = ∂L/∂x`. -/
def IsEL (L : ScalarLagrangian) (γ : ℝ → ℝ) : Prop :=
  ∀ t, deriv (fun s => momentum L s (γ s) (deriv γ s)) t
        = gradX L t (γ t) (deriv γ t)

/-- The conservative Lagrangian `L = T - U` with `T = ½ m v²`. -/
noncomputable def freeLag (m : ℝ) (U : ℝ → ℝ) : ScalarLagrangian :=
  fun _ x v => (m / 2) * v ^ 2 - U x

/-- Newton's second law `m γ'' = -U'(γ)` in one dimension. -/
def IsNewtonian (m : ℝ) (U : ℝ → ℝ) (γ : ℝ → ℝ) : Prop :=
  ∀ t, m * deriv (deriv γ) t = - deriv U (γ t)

/-- The derivative of `x ↦ x²` is `2x`. -/
theorem hasDerivAt_sq (x : ℝ) : HasDerivAt (fun w : ℝ => w ^ 2) (2 * x) x := by
  simpa using hasDerivAt_pow 2 x

/-- The generalized momentum of a conservative Lagrangian is `m v`. -/
theorem momentum_freeLag (m : ℝ) (U : ℝ → ℝ) (t x v : ℝ) :
    momentum (freeLag m U) t x v = m * v := by
  unfold momentum freeLag
  have h1 : HasDerivAt (fun w : ℝ => (m / 2) * w ^ 2) (m * v) v := by
    have := (hasDerivAt_sq v).const_mul (m / 2)
    convert this using 1
    ring
  have h2 : HasDerivAt (fun _ : ℝ => U x) 0 v := hasDerivAt_const v (U x)
  have h := h1.sub h2
  simpa using h.deriv

/-- The generalized force of a conservative Lagrangian is `-U'`. -/
theorem gradX_freeLag (m : ℝ) (U : ℝ → ℝ) (x : ℝ) (hU : DifferentiableAt ℝ U x)
    (t v : ℝ) : gradX (freeLag m U) t x v = - deriv U x := by
  unfold gradX freeLag
  have h1 : HasDerivAt (fun _ : ℝ => (m / 2) * v ^ 2) 0 x := hasDerivAt_const x _
  have h2 : HasDerivAt U (deriv U x) x := hU.hasDerivAt
  have h := h1.sub h2
  simpa using h.deriv

/-- Pointwise version of `momentum_freeLag`, suitable for rewriting under a
`deriv`. -/
theorem momentum_freeLag_fun (m : ℝ) (U : ℝ → ℝ) (γ : ℝ → ℝ) :
    (fun s => momentum (freeLag m U) s (γ s) (deriv γ s)) = fun s => m * deriv γ s := by
  funext s
  rw [momentum_freeLag]

/-- **Newton ⇔ Euler–Lagrange** for a conservative Lagrangian in Cartesian
coordinates.  This is the first link of the equivalence chain. -/
theorem isEL_freeLag_iff_newtonian (m : ℝ) (U : ℝ → ℝ) (γ : ℝ → ℝ)
    (hU : ∀ x, DifferentiableAt ℝ U x) (hγ : Differentiable ℝ (deriv γ)) :
    IsEL (freeLag m U) γ ↔ IsNewtonian m U γ := by
  unfold IsEL IsNewtonian
  constructor
  · intro h t
    have hel := h t
    rw [momentum_freeLag_fun, deriv_const_mul m (hγ t),
        gradX_freeLag m U (γ t) (hU (γ t))] at hel
    exact hel
  · intro h t
    rw [momentum_freeLag_fun, deriv_const_mul m (hγ t),
        gradX_freeLag m U (γ t) (hU (γ t))]
    exact h t

/-- The harmonic-oscillator potential `U = ½ k x²`. -/
noncomputable def harmonicPotential (k : ℝ) : ℝ → ℝ := fun x => (k / 2) * x ^ 2

/-- The harmonic potential is differentiable everywhere. -/
theorem differentiableAt_harmonicPotential (k x : ℝ) :
    DifferentiableAt ℝ (harmonicPotential k) x := by
  unfold harmonicPotential
  fun_prop

/-- The derivative of the harmonic potential is `k x`. -/
theorem deriv_harmonicPotential (k x : ℝ) : deriv (harmonicPotential k) x = k * x := by
  unfold harmonicPotential
  have h1 : HasDerivAt (fun x : ℝ => (k / 2) * x ^ 2) (k * x) x := by
    have := (hasDerivAt_sq x).const_mul (k / 2)
    convert this using 1
    ring
  simpa using h1.deriv

/-- **Harmonic oscillator equation of motion**: the Euler–Lagrange equation for
`L = ½ m v² - ½ k x²` is `m γ'' + k γ = 0`. -/
theorem harmonic_oscillator_eom (m k : ℝ) (γ : ℝ → ℝ)
    (hγ : Differentiable ℝ (deriv γ)) :
    IsEL (freeLag m (harmonicPotential k)) γ ↔
      ∀ t, m * deriv (deriv γ) t + k * γ t = 0 := by
  rw [isEL_freeLag_iff_newtonian m (harmonicPotential k) γ
        (fun x => differentiableAt_harmonicPotential k x) hγ]
  unfold IsNewtonian
  constructor
  · intro h t
    have := h t
    rw [deriv_harmonicPotential] at this
    linarith
  · intro h t
    have := h t
    rw [deriv_harmonicPotential]
    linarith

end FormalPhysics.Lagrangian
