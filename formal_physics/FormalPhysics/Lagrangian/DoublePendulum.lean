/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Taylor §7.7 — The Double Pendulum

The double pendulum is the canonical coupled system whose Lagrangian is
`L = T - U` with a cross term `θ̇₁θ̇₂ cos(θ₁ - θ₂)`.  We record the kinetic
energy, potential, and Lagrangian, and check the defining identity.
-/
import Mathlib

namespace FormalPhysics.Lagrangian

/-- Kinetic energy of a planar double pendulum with angles `θ₁, θ₂`. -/
noncomputable def doublePendulumT (m1 m2 l1 l2 th1 th2 dth1 dth2 : ℝ) : ℝ :=
  (1 / 2) * (m1 + m2) * l1 ^ 2 * dth1 ^ 2
    + (1 / 2) * m2 * l2 ^ 2 * dth2 ^ 2
    + m2 * l1 * l2 * dth1 * dth2 * Real.cos (th1 - th2)

/-- Potential energy of a planar double pendulum with gravity `g`. -/
noncomputable def doublePendulumU (m1 m2 l1 l2 g th1 th2 : ℝ) : ℝ :=
  -((m1 + m2) * g * l1 * Real.cos th1) - m2 * g * l2 * Real.cos th2

/-- The double-pendulum Lagrangian `L = T - U`. -/
noncomputable def doublePendulumL (m1 m2 l1 l2 g th1 th2 dth1 dth2 : ℝ) : ℝ :=
  doublePendulumT m1 m2 l1 l2 th1 th2 dth1 dth2
    - doublePendulumU m1 m2 l1 l2 g th1 th2

/-- The Lagrangian is, by definition, kinetic minus potential energy. -/
theorem doublePendulumL_def (m1 m2 l1 l2 g th1 th2 dth1 dth2 : ℝ) :
    doublePendulumL m1 m2 l1 l2 g th1 th2 dth1 dth2
      = doublePendulumT m1 m2 l1 l2 th1 th2 dth1 dth2
        - doublePendulumU m1 m2 l1 l2 g th1 th2 := rfl

/-- At the bottom configuration `θ₁ = θ₂ = 0` the cross term is maximal and the
kinetic energy simplifies. -/
theorem doublePendulumT_at_rest (m1 m2 l1 l2 dth1 dth2 : ℝ) :
    doublePendulumT m1 m2 l1 l2 0 0 dth1 dth2
      = (1 / 2) * (m1 + m2) * l1 ^ 2 * dth1 ^ 2
        + (1 / 2) * m2 * l2 ^ 2 * dth2 ^ 2
        + m2 * l1 * l2 * dth1 * dth2 := by
  unfold doublePendulumT
  simp [Real.cos_zero]

end FormalPhysics.Lagrangian
