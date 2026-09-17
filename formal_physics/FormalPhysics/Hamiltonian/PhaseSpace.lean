/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Phase Space and Hamilton's Equations

A Hamiltonian is a scalar on phase space; Hamilton's equations are first-order
ODEs for the pair `(q, p)`.  We formalize phase space, the partial derivatives
`∂H/∂q`, `∂H/∂p`, Hamilton's equations as a predicate on curves, and prove that
for the harmonic oscillator the Hamiltonian is conserved along the flow.
-/
import Mathlib
import FormalPhysics.Calculus

namespace FormalPhysics.Hamiltonian

open FormalPhysics

/-- Phase space for one degree of freedom, written as a pair of scalars. -/
abbrev PhaseSpace := ℝ × ℝ

/-- `∂H/∂q`. -/
noncomputable def pdq (H : ℝ → ℝ → ℝ) (q p : ℝ) : ℝ := deriv (fun q' => H q' p) q

/-- `∂H/∂p`. -/
noncomputable def pdp (H : ℝ → ℝ → ℝ) (q p : ℝ) : ℝ := deriv (fun p' => H q p') p

/-- **Hamilton's equations** as a predicate on a pair of curves `(q, p)`:
`q̇ = ∂H/∂p` and `ṗ = -∂H/∂q`. -/
def IsHamiltonFlow (H : ℝ → ℝ → ℝ) (q p : ℝ → ℝ) : Prop :=
  ∀ t, HasDerivAt q (pdp H (q t) (p t)) t ∧
       HasDerivAt p (-(pdq H (q t) (p t))) t

/-- The harmonic-oscillator Hamiltonian `H = p²/(2m) + ½ k q²`. -/
noncomputable def harmonicH (m k : ℝ) (q p : ℝ) : ℝ :=
  (1 / (2 * m)) * p ^ 2 + (k / 2) * q ^ 2

/-- `∂H/∂p = p/m` for the harmonic oscillator. -/
theorem pdp_harmonicH (m k q p : ℝ) :
    pdp (harmonicH m k) q p = p / m := by
  unfold pdp harmonicH
  have h1 : HasDerivAt (fun p' : ℝ => (1 / (2 * m)) * p' ^ 2)
      ((1 / (2 * m)) * (2 * p)) p :=
    (hasDerivAt_sq p).const_mul (1 / (2 * m))
  have h2 : HasDerivAt (fun _ : ℝ => (k / 2) * q ^ 2) 0 p := hasDerivAt_const p _
  have h := h1.add h2
  rw [h.deriv]
  field_simp
  ring

/-- `∂H/∂q = k q` for the harmonic oscillator. -/
theorem pdq_harmonicH (m k q p : ℝ) :
    pdq (harmonicH m k) q p = k * q := by
  unfold pdq harmonicH
  have h1 : HasDerivAt (fun _ : ℝ => (1 / (2 * m)) * p ^ 2) 0 q := hasDerivAt_const q _
  have h2 : HasDerivAt (fun q' : ℝ => (k / 2) * q' ^ 2)
      ((k / 2) * (2 * q)) q :=
    (hasDerivAt_sq q).const_mul (k / 2)
  have h := h1.add h2
  rw [h.deriv]
  ring

/-- Hamilton's equations for the harmonic oscillator reduce to the familiar
first-order system `q̇ = p/m`, `ṗ = -k q`. -/
theorem hamilton_flow_harmonic (m k : ℝ) (q p : ℝ → ℝ) :
    IsHamiltonFlow (harmonicH m k) q p ↔
      ∀ t, HasDerivAt q (p t / m) t ∧ HasDerivAt p (-(k * q t)) t := by
  unfold IsHamiltonFlow
  constructor
  · intro h t
    have ht := h t
    simp only [pdp_harmonicH, pdq_harmonicH] at ht
    exact ht
  · intro h t
    simp only [pdp_harmonicH, pdq_harmonicH]
    exact h t

/-- **Conservation of energy** for the harmonic oscillator: along any solution
of Hamilton's equations the Hamiltonian is constant. -/
theorem energy_conserved_harmonic (m k : ℝ) (hm : m ≠ 0) (q p : ℝ → ℝ)
    (hq : ∀ t, HasDerivAt q (p t / m) t)
    (hp : ∀ t, HasDerivAt p (-(k * q t)) t) :
    ∀ t, deriv (fun t => harmonicH m k (q t) (p t)) t = 0 := by
  intro t
  have hp2 : HasDerivAt (fun t => (p t) ^ 2) (2 * p t * (-(k * q t))) t := by
    have := (hp t).pow 2
    simpa [pow_one] using this
  have hq2 : HasDerivAt (fun t => (q t) ^ 2) (2 * q t * (p t / m)) t := by
    have := (hq t).pow 2
    simpa [pow_one] using this
  have h := (hp2.const_mul (1 / (2 * m))).add (hq2.const_mul (k / 2))
  have hval : (1 / (2 * m)) * (2 * p t * (-(k * q t)))
      + (k / 2) * (2 * q t * (p t / m)) = 0 := by
    field_simp
    ring
  change deriv (fun t => (1 / (2 * m)) * (p t) ^ 2 + (k / 2) * (q t) ^ 2) t = 0
  rw [h.deriv, hval]

end FormalPhysics.Hamiltonian
