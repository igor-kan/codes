# Quantum Field Theory & S-Matrix Scattering Package

Rigorous implementation of relativistic quantum field theory and S-matrix scattering algorithms based on Landau & Lifshitz Vol 4 (*Quantum Electrodynamics*), Chow (*Mathematical Methods for Physicists*), and Blennow (*Mathematical Methods for Physics and Engineering*).

## Modules
1. **dirac_matrices.py**: Dirac gamma matrices in Dirac-Pauli and Weyl representations; Clifford algebra verification.
2. **feynman_slash.py**: Feynman slash notation, Minkowski dot products, Dirac trace theorems.
3. **mandelstam_variables.py**: Relativistic 2-to-2 scattering kinematics and Mandelstam sum rule.
4. **klein_gordon_propagator.py**: Spin-0 scalar Feynman propagator and spacelike exponential decay.
5. **dirac_propagator.py**: Spin-1/2 Dirac propagator and positive/negative energy projectors.
6. **photon_polarization_sum.py**: Transverse photon completeness relation and Ward identity.
7. **moller_scattering.py**: Tree-level QED electron-electron scattering differential cross section.
8. **bhabha_scattering.py**: Tree-level QED electron-positron scattering cross section.
9. **compton_scattering_klein_nishina.py**: Klein-Nishina Compton scattering cross section.
10. **breit_wigner_resonance.py**: Relativistic Breit-Wigner lineshape and Z-boson resonance.
11. **gordon_decomposition.py**: Dirac current decomposition into convective and spin-magnetization terms.
12. **casimir_invariants_poincare.py**: Poincaré algebra Casimir operators (mass-squared, Pauli-Lubanski).
13. **passarino_veltman_reduction.py**: 1-loop tensor reduction into scalar integrals.
14. **dimensional_regularization.py**: D-dimensional pole extraction and MS-bar renormalization scale.
15. **running_coupling_qed.py**: Renormalization group running fine-structure constant and Landau pole.

## Testing
Run unit tests with pytest:
```bash
pytest algorithms/01_python/quantum_field_theory_and_s_matrix/
```
