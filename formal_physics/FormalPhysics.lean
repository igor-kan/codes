/-
Copyright (c) 2026 Igor Kan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Igor Kan

# Formal Physics — Analytical Classical Mechanics

A Lean 4 / Mathlib formalization of foundational analytical mechanics:

* **Calculus of Variations** — functionals, first and second variation,
  the Euler–Lagrange equation, the Beltrami identity, the brachistochrone
  and the cycloid.
* **Lagrangian Mechanics** — configuration space, generalized momentum,
  Newton ⇔ Euler–Lagrange equivalence, curvilinear coordinates,
  rheonomic kinetic energy, Hamilton's principle, constraints and
  Noether's theorem.
* **Hamiltonian Mechanics** — phase space, Hamilton's equations,
  the Legendre transform, the Poisson bracket, the symplectic form and
  Liouville's theorem.
-/
import FormalPhysics.Calculus
import FormalPhysics.Variations.Basic
import FormalPhysics.Variations.Beltrami
import FormalPhysics.Variations.Brachistochrone
import FormalPhysics.Variations.SecondVariation
import FormalPhysics.Variations.SeveralVariables
import FormalPhysics.Lagrangian.EulerLagrange
import FormalPhysics.Lagrangian.Configuration
import FormalPhysics.Lagrangian.Coordinates
import FormalPhysics.Lagrangian.Noether
import FormalPhysics.Lagrangian.HamiltonPrinciple
import FormalPhysics.Lagrangian.Constraints
import FormalPhysics.Lagrangian.DoublePendulum
import FormalPhysics.Hamiltonian.PhaseSpace
import FormalPhysics.Hamiltonian.Legendre
import FormalPhysics.Hamiltonian.Poisson
import FormalPhysics.Hamiltonian.Symplectic
import FormalPhysics.Hamiltonian.Liouville
