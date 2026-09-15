/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Taylor §13.6–13.7 — Liouville's Theorem

A Hamiltonian flow is incompressible in phase space: it preserves volume.  For a
linear (small-oscillation) flow the statement becomes `det M = 1`, where `M` is
the one-period time-evolution matrix.  We verify this for the harmonic-oscillator
rotation matrix.
-/
import Mathlib

namespace FormalPhysics.Hamiltonian

open Matrix

/-- The harmonic-oscillator time-evolution matrix
`M = [[cos ωt, (1/ω) sin ωt], [-ω sin ωt, cos ωt]]`. -/
noncomputable def flowMatrix (ω t : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![Real.cos (ω * t), (1 / ω) * Real.sin (ω * t);
     -(ω) * Real.sin (ω * t), Real.cos (ω * t)]

/-- **Liouville / area preservation**: the flow matrix has unit determinant, so
Hamiltonian flow preserves phase-space area. -/
theorem det_flowMatrix (ω t : ℝ) (hω : ω ≠ 0) : (flowMatrix ω t).det = 1 := by
  rw [Matrix.det_fin_two]
  simp [flowMatrix]
  field_simp [hω]
  linear_combination ω * Real.sin_sq_add_cos_sq (ω * t)

end FormalPhysics.Hamiltonian
