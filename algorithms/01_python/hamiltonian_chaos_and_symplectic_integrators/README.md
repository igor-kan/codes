# Hamiltonian Chaos & Symplectic Integrators Package

A research-grade computational library of symplectic geometric integrators, KAM theory, and nonlinear Hamiltonian chaos based on Arnold (*Mathematical Methods of Classical Mechanics*) and Gershenfeld (*The Nature of Mathematical Modeling*).

## Modules
1. **symplectic_verlet.py**: Velocity Verlet and Störmer-Verlet area-preserving integrators.
2. **yoshida_fourth_order.py**: Explicit 4th-order Yoshida symplectic composition integrator.
3. **henon_heiles_hamiltonian.py**: Hénon-Heiles galactic potential and Poincaré section.
4. **chirikov_standard_map.py**: Chirikov standard map, kicked rotor, and golden KAM boundary.
5. **lyapunov_spectrum_hamiltonian.py**: Benettin tangent space maximal Lyapunov exponent.
6. **kam_torus_action_angle.py**: Diophantine non-resonance condition for invariant KAM tori.
7. **fermi_pasta_ulam_tsingou.py**: FPUT nonlinear lattice soliton quasi-periodic recurrence.
8. **birkhoff_normal_form.py**: Birkhoff normal form anharmonic tune shift and island width.
9. **poincare_recurrence.py**: Discrete phase space Poincaré recurrence time tracking.
10. **arnold_cat_map.py**: Arnold cat map hyperbolic torus automorphism and Lyapunov exponent.
11. **melnikov_integral_chaos.py**: Melnikov integral for transverse homoclinic bifurcations.
12. **forest_ruth_fourth_order.py**: Forest-Ruth 4th-order symplectic integration coefficients.
13. **symplectic_two_body_kepler.py**: Symplectic Kepler orbit and Laplace-Runge-Lenz conservation.
14. **nekhoroshev_stability.py**: Nekhoroshev exponential stability timescale estimates.
15. **canonical_perturbation_theory.py**: Fast-angle averaging and secular drift elimination.

## Testing
Run unit tests with pytest:
```bash
pytest algorithms/01_python/hamiltonian_chaos_and_symplectic_integrators/
```
