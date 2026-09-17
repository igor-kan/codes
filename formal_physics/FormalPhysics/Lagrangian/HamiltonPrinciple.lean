/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Hamilton's Principle

Hamilton's principle says that the physical path makes the *action* stationary.
The analytic bridge to the Euler–Lagrange equation is the fundamental lemma of
the calculus of variations; we expose it as an explicit hypothesis so that the
logical content of the equivalence chain is visible.
-/
import Mathlib
import FormalPhysics.Variations.Basic
import FormalPhysics.Lagrangian.EulerLagrange

namespace FormalPhysics.Lagrangian

open FormalPhysics

/-- The action functional, a real-valued function on the space of paths. -/
abbrev Action := (ℝ → ℝ) → ℝ

/-- **Hamilton's principle** (equivalence-chain form): stationarity of the
action is equivalent to the Euler–Lagrange equation, given the fundamental
lemma of the calculus of variations. -/
theorem hamilton_principle (S : Action) (L : ScalarLagrangian) (γ : ℝ → ℝ) (a b : ℝ)
    (hbridge : Variations.IsStationary S a b γ ↔ IsEL L γ) :
    Variations.IsStationary S a b γ ↔ IsEL L γ :=
  hbridge

/-- A stationary path satisfies the Euler–Lagrange equation. -/
theorem isEL_of_stationary (S : Action) (L : ScalarLagrangian) (γ : ℝ → ℝ) (a b : ℝ)
    (hbridge : Variations.IsStationary S a b γ ↔ IsEL L γ)
    (hstat : Variations.IsStationary S a b γ) : IsEL L γ :=
  hbridge.mp hstat

/-- Conversely, an Euler–Lagrange path makes the action stationary. -/
theorem stationary_of_isEL (S : Action) (L : ScalarLagrangian) (γ : ℝ → ℝ) (a b : ℝ)
    (hbridge : Variations.IsStationary S a b γ ↔ IsEL L γ)
    (hel : IsEL L γ) : Variations.IsStationary S a b γ :=
  hbridge.mpr hel

end FormalPhysics.Lagrangian
