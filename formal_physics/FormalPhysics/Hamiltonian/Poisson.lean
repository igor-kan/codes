/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Taylor §13.5 — The Poisson Bracket

For one degree of freedom the Poisson bracket of two observables is

  `{f, g} = ∂f/∂q ∂g/∂p - ∂f/∂p ∂g/∂q`.

We verify the algebraic axioms — antisymmetry, the bracket of a function with
itself vanishes, and the canonical coordinate brackets `{q,p} = 1` — and record
the Jacobi identity as a named hypothesis structure, since its proof for general
smooth functions uses the symmetry of second derivatives.
-/
import Mathlib
import FormalPhysics.Calculus

namespace FormalPhysics.Hamiltonian

open FormalPhysics

/-- The canonical Poisson bracket on phase space `ℝ × ℝ`. -/
noncomputable def poisson (f g : ℝ → ℝ → ℝ) (q p : ℝ) : ℝ :=
  deriv (fun q' => f q' p) q * deriv (fun p' => g q p') p
    - deriv (fun p' => f q p') p * deriv (fun q' => g q' p) q

/-- The bracket as a function of phase space. -/
noncomputable def poissonFun (f g : ℝ → ℝ → ℝ) : ℝ → ℝ → ℝ :=
  fun q p => poisson f g q p

/-- **Antisymmetry**: `{f, g} = -{g, f}`. -/
theorem poisson_antisymm (f g : ℝ → ℝ → ℝ) (q p : ℝ) :
    poisson f g q p = - poisson g f q p := by
  unfold poisson; ring

/-- The bracket of a function with itself vanishes. -/
theorem poisson_self (f : ℝ → ℝ → ℝ) (q p : ℝ) : poisson f f q p = 0 := by
  unfold poisson; ring

/-- The bracket with a constant function vanishes (on the right). -/
theorem poisson_const_right (f : ℝ → ℝ → ℝ) (c q p : ℝ) :
    poisson f (fun _ _ => c) q p = 0 := by
  unfold poisson
  simp [deriv_const_eq]

/-- The bracket with a constant function vanishes (on the left). -/
theorem poisson_const_left (g : ℝ → ℝ → ℝ) (c q p : ℝ) :
    poisson (fun _ _ => c) g q p = 0 := by
  unfold poisson
  simp [deriv_const_eq]

/-- The canonical bracket of the coordinate functions: `{q, p} = 1`. -/
theorem poisson_coord_qp (q p : ℝ) :
    poisson (fun a _ => a) (fun _ b => b) q p = 1 := by
  unfold poisson
  simp [deriv_id_eq, deriv_const_eq]

/-- `{p, q} = -1`. -/
theorem poisson_coord_pq (q p : ℝ) :
    poisson (fun _ b => b) (fun a _ => a) q p = -1 := by
  unfold poisson
  simp [deriv_id_eq, deriv_const_eq]

/-- A structure recording the axioms of a Poisson bracket; the canonical
bracket satisfies antisymmetry and the product rule, and the Jacobi identity
holds for smooth observables (it is the symmetry of second derivatives). -/
structure IsPoissonBracket (bracket : (ℝ → ℝ → ℝ) → (ℝ → ℝ → ℝ) → ℝ → ℝ → ℝ) : Prop where
  antisymm : ∀ f g q p, bracket f g q p = - bracket g f q p
  self_zero : ∀ f q p, bracket f f q p = 0
  jacobi : ∀ f g h q p,
    bracket f (poissonFun g h) q p + bracket g (poissonFun h f) q p
      + bracket h (poissonFun f g) q p = 0

/-- The canonical bracket is antisymmetric and vanishes on equal arguments. -/
theorem poisson_antisymm_and_self :
    (∀ f g q p, poisson f g q p = - poisson g f q p) ∧
    (∀ f q p, poisson f f q p = 0) :=
  ⟨poisson_antisymm, poisson_self⟩

end FormalPhysics.Hamiltonian
