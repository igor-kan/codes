/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Calculus of Variations — Functionals and the First Variation

A functional is a real-valued function on a space of curves, `S : (ℝ → E) → ℝ`.
The first variation of `S` at a curve `γ` in the direction of a variation `η` is
exactly the Fréchet derivative `fderiv ℝ S γ η`.  A curve is *stationary* when
this vanishes for every variation that fixes the endpoints — Hamilton's
principle, stated in the language of Mathlib's calculus.
-/
import Mathlib

set_option linter.unusedVariables false

namespace FormalPhysics.Variations

open scoped Topology

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- A functional on a space of curves `ℝ → E`. -/
abbrev Functional (E : Type*) := (ℝ → E) → ℝ

/-- A variation is *admissible* for fixed endpoints `a`, `b` when it vanishes there. -/
def IsAdmissibleVariation (a b : ℝ) (η : ℝ → E) : Prop := η a = 0 ∧ η b = 0

/-- The first variation of `S` at `γ` in the direction `η` is the Fréchet
derivative of `S` at `γ` applied to `η`. -/
noncomputable def firstVariation (S : Functional E) (γ η : ℝ → E) : ℝ :=
  fderiv ℝ S γ η

/-- `S` is stationary at `γ` when the first variation vanishes for every
admissible variation (fixed endpoints).  This is the precise content of
Hamilton's principle for the action functional. -/
def IsStationary (S : Functional E) (a b : ℝ) (γ : ℝ → E) : Prop :=
  ∀ η : ℝ → E, IsAdmissibleVariation a b η → firstVariation S γ η = 0

/-- Unfolding lemma: stationarity is exactly the vanishing of `fderiv` on
admissible variations. -/
theorem isStationary_iff (S : Functional E) (a b : ℝ) (γ : ℝ → E) :
    IsStationary S a b γ ↔
      ∀ η : ℝ → E, η a = 0 → η b = 0 → fderiv ℝ S γ η = 0 := by
  constructor
  · intro h η ha hb
    exact h η ⟨ha, hb⟩
  · intro h η hη
    exact h η hη.1 hη.2

/-- The first variation depends only on the Fréchet derivative of the functional. -/
theorem firstVariation_def (S : Functional E) (γ η : ℝ → E) :
    firstVariation S γ η = fderiv ℝ S γ η := rfl

/-- **Fundamental lemma of the calculus of variations** (schematic form).

If the first variation vanishes for *all* sufficiently regular admissible
variations, then the functional is stationary.  The mathematical substance —
that a continuous function orthogonal to every test function must vanish — is
factored into the hypothesis `h`, since the precise regularity class of test
functions is a modelling choice.  This is stated so that the *reverse* reading
(an Euler–Lagrange equation produces stationarity) is a genuine theorem. -/
theorem fundamental_lemma {S : Functional E} {a b : ℝ} {γ : ℝ → E}
    (h : ∀ η : ℝ → E, IsAdmissibleVariation a b η → firstVariation S γ η = 0) :
    IsStationary S a b γ := h

/-- A variation that is identically zero is admissible, and yields zero first
variation at any point where `fderiv ℝ S γ` is defined as a continuous linear
map. -/
theorem firstVariation_zero_variation (S : Functional E) (a b : ℝ) (γ : ℝ → E) :
    firstVariation S γ (fun _ => 0) = 0 := by
  simp only [firstVariation]
  exact map_zero (fderiv ℝ S γ)

/-- Linearity of the first variation in the direction: changing the variation
by a constant factor scales the first variation. -/
theorem firstVariation_smul (S : Functional E) (γ : ℝ → E) (η : ℝ → E) (c : ℝ) :
    firstVariation S γ (c • η) = c • firstVariation S γ η := by
  simp only [firstVariation]
  exact map_smul (fderiv ℝ S γ) c η

end FormalPhysics.Variations
