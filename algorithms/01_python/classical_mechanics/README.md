# Advanced Classical Mechanics Mathematical Formalisms

A rigorous implementation of advanced mathematical formalisms and geometric mechanics based on:
- **V.I. Arnold**, *Mathematical Methods of Classical Mechanics* (Graduate Texts in Mathematics, Springer).
- **L.D. Landau & E.M. Lifshitz**, *Mechanics* (Course of Theoretical Physics, Vol. 1, Butterworth-Heinemann).
- **John R. Taylor**, *Classical Mechanics* (University Science Books).

## Architecture & Mathematical Objects

The modules encapsulate classical mechanics across Hamiltonian symplectic geometry, Lagrangian variational mechanics, integrable systems, non-holonomic systems, and geometric perturbation theory:

| Category | Module / Class | Theoretical Reference |
| :--- | :--- | :--- |
| **Symplectic Geometry** | [`SymplecticManifold`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/symplectic_manifold.py) | Arnold §16: Symplectic 2-form $\omega = \sum dq^i \wedge dp_i$ and condition $M^T J M = J$ |
| | [`PoissonBracket`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/poisson_bracket.py) | Arnold §18: Poisson bracket $\{f, g\}_{\text{PB}}$ and Jacobi identity verification |
| | [`HamiltonianVectorField`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/hamiltonian_vector_field.py) | Arnold §16: $i_{X_H}\omega = -dH$, flow equations, and Liouville theorem $\text{div}(X_H) = 0$ |
| | [`CanonicalTransformation`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/canonical_transformations.py) | Arnold §45, Landau §45: Generating functions $F_1, F_2, F_3, F_4$ |
| | [`HamiltonJacobiSolver`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/hamilton_jacobi_equation.py) | Landau §47: Hamilton's characteristic function $W(q, \alpha)$ and action integrals |
| | [`ActionAngleTorus`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/action_angle_variables.py) | Arnold §50: Arnold-Liouville theorem, invariant tori $\mathbb{T}^n$, and resonance |
| | [`ContactGeometry`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/contact_geometry.py) | Arnold App. 4: Odd-dimensional contact 1-form $\alpha$, Reeb field, and dissipation |
| **Variational & Symmetries** | [`LegendreTransform`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/legendre_transform.py) | Arnold §14: Fenchel-Legendre duality between $L(q, \dot{q})$ and $H(q, p)$ |
| | [`EulerLagrangeSystem`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/euler_lagrange_equations.py) | Landau §1-§5, Taylor §6: Variational equations and cyclic coordinates |
| | [`NoetherTheorem`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/noether_theorem.py) | Arnold §20, Landau §6-§9: Symmetries, conserved charges, and Runge-Lenz vector |
| | [`MaupertuisJacobiMetric`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/maupertuis_principle.py) | Arnold §37: Maupertuis principle and Riemannian geodesics of Jacobi metric |
| | [`DAlembertPrinciple`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/d_alembert_lagrange_principle.py) | Arnold §17: D'Alembert virtual work $\sum (\mathbf{F}_i - m_i \ddot{\mathbf{r}}_i) \cdot \delta \mathbf{r}_i = 0$ |
| | [`AppellsMechanics`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/appells_equations.py) | Gibbs-Appell equations via energy of acceleration $S = \frac{1}{2}\sum m_i \ddot{\mathbf{r}}_i^2$ |
| **Rigid Body Kinematics** | [`PoinsotConstruction`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/poinsot_ellipsoid.py) | Landau §37: Inertia ellipsoid rolling on invariable plane, polhode/herpolhode |
| | [`EulerRigidBody`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/euler_equations_rigid_body.py) | Landau §36, Taylor §10.8: Intermediate axis instability (Dzhanibekov effect) |
| | [`EulerAnglesKinematics`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/euler_angles_kinematics.py) | Landau §35, Taylor §10.3: $Z$-$X$-$Z$ proper convention and body velocity mapping |
| | [`QuaternionRigidBody`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/quaternion_rigid_body.py) | $S^3 \cong \text{Spin}(3)$ unit quaternion attitude propagation without gimbal lock |
| | [`LiePoissonRigidBody`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/rigid_body_lie_poisson.py) | Arnold §47: Lie-Poisson reduction on $\mathfrak{so}(3)^*$ and Casimir $C = \frac{1}{2}\|\mathbf{m}\|^2$ |
| **Integrable Systems & Chaos** | [`CalogeroMoserSystem`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/integrable_systems_calogero_moser.py) | Lax pair $L, M$, Lax equation $\dot{L} = [M, L]$, and conserved trace invariants |
| | [`TodaLattice`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/toda_lattice.py) | Flaschka tridiagonal Lax representation and Toda solitary wave invariants |
| | [`ChirikovStandardMap`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/kam_theorem_mapping.py) | KAM theorem: Area-preserving standard map and invariant tori breakdown |
| | [`PoincareSection`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/poincare_surface_of_section.py) | Transverse section analysis: KAM regular islands vs ergodic chaotic wandering |
| **Oscillations & Perturbation** | [`SmallOscillations`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/small_oscillations.py) | Taylor §11, Landau §23: Generalized eigenvalue problem $(K - \omega^2 M) a = 0$ |
| | [`AnharmonicOscillator`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/anharmonic_oscillators.py) | Landau §28: Poincaré-Lindstedt perturbation method and frequency shift $\Delta \omega(A)$ |
| | [`AdiabaticInvariantOscillator`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/adiabatic_invariants.py) | Landau §49, Arnold §48: Adiabatic invariance $E(t)/\omega(t) \approx \text{const}$ |
| **Geodesics & Geometric Phase** | [`KeplerOrbitGeometry`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/kepler_orbit_geometry.py) | Arnold §8, Taylor §8: Kepler's equation $M = E - e \sin E$ and orbital anomalies |
| | [`FoucaultPendulumGeometricPhase`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/foucault_pendulum_geometric_phase.py) | Arnold §24: Hannay angle and Berry geometric phase $\Delta \psi = 2\pi(1 - \sin\lambda)$ |
| | [`NonHolonomicSystem`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/nonholonomic_constraints.py) | Pfaffian non-holonomic velocity constraints $A(q)\dot{q} = 0$ |
| | [`SymplecticIntegrator`](file:///home/igorkan/repos/codes/algorithms/01_python/classical_mechanics/poisson_integrator_symplectic.py) | Geometric numerical integration: Störmer-Verlet, Ruth, and shadow Hamiltonian conservation |
