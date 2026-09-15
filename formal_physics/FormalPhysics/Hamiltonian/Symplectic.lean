/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Taylor Ch. 13 — The Symplectic Form

The Hamiltonian vector field is produced by contracting the differential of the
Hamiltonian with the symplectic form.  In one degree of freedom this form is the
linear map `J(q, p) = (p, -q)`.  We verify that it is skew with respect to the
inner product, nondegenerate, and satisfies `J² = -1`.
-/
import Mathlib

namespace FormalPhysics.Hamiltonian

/-- The symplectic operator `J(q, p) = (p, -q)` on phase space. -/
noncomputable def J (z : ℝ × ℝ) : ℝ × ℝ := (z.2, -z.1)

/-- `J² = -1`. -/
theorem J_sq (z : ℝ × ℝ) : J (J z) = -z := by
  ext <;> simp [J]

/-- Componentwise description of `J`. -/
theorem J_fst (z : ℝ × ℝ) : (J z).1 = z.2 := rfl

/-- Componentwise description of `J`. -/
theorem J_snd (z : ℝ × ℝ) : (J z).2 = -z.1 := rfl

/-- `J` is injective, hence the symplectic form is nondegenerate. -/
theorem J_injective : Function.Injective J := by
  intro a b h
  have h1 : a.2 = b.2 := by simpa [J] using congrArg Prod.fst h
  have h2 : a.1 = b.1 := by
    have := congrArg Prod.snd h
    simp [J] at this
    linarith
  exact Prod.ext h2 h1

/-- The only element in the kernel is zero: nondegeneracy. -/
theorem J_kernel (z : ℝ × ℝ) (h : J z = 0) : z = 0 := by
  apply J_injective
  rw [h]
  simp [J]

/-- The symplectic form is skew, written componentwise:
`⟨Jz, w⟩ + ⟨z, Jw⟩ = 0`. -/
theorem J_skew (z w : ℝ × ℝ) :
    (J z).1 * w.1 + (J z).2 * w.2 + (z.1 * (J w).1 + z.2 * (J w).2) = 0 := by
  simp [J]
  ring

end FormalPhysics.Hamiltonian
