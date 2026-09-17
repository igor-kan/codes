# Nonlinear Dynamics, Solitons & Chaos

A comprehensive Python suite of algorithms for nonlinear ordinary and partial differential equations, chaotic attractors, solitary waves (solitons), phase synchronization, and bifurcation theory.

## Modules

1. **[`lorenz_attractor_rk4.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/lorenz_attractor_rk4.py)**: Classical Lorenz butterfly strange attractor integrator ($\sigma=10, \rho=28, \beta=8/3$).
2. **[`rossler_attractor.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/rossler_attractor.py)**: Rössler system continuous chaotic flow ($a=0.2, b=0.2, c=5.7$).
3. **[`lyapunov_exponent_spectrum.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/lyapunov_exponent_spectrum.py)**: Maximal Lyapunov exponent $\lambda_{\text{max}}$ via trajectory perturbation and Benettin renormalization.
4. **[`korteveg_de_vries_soliton.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/korteveg_de_vries_soliton.py)**: Korteweg-de Vries (KdV) exact single soliton and conserved energy integrals.
5. **[`sine_gordon_kink_breather.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/sine_gordon_kink_breather.py)**: Sine-Gordon topological kinks, anti-kinks, and localized oscillating breathers.
6. **[`nonlinear_schrodinger_soliton.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/nonlinear_schrodinger_soliton.py)**: 1D Nonlinear Schrödinger Equation (NLSE) fundamental bright and dark solitary waves.
7. **[`kuramoto_oscillators_sync.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/kuramoto_oscillators_sync.py)**: Kuramoto phase synchronization model and complex order parameter $r e^{i\psi}$.
8. **[`hopf_bifurcation.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/hopf_bifurcation.py)**: Supercritical and subcritical Hopf bifurcation normal forms and limit cycle radii.
9. **[`pitchfork_transcritical_bifurcations.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/pitchfork_transcritical_bifurcations.py)**: Saddle-node, transcritical, and supercritical pitchfork fixed-point branches.
10. **[`duffing_chaotic_oscillator.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/duffing_chaotic_oscillator.py)**: Periodically driven, damped non-linear double-well Duffing oscillator.
11. **[`van_der_pol_relaxation.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/van_der_pol_relaxation.py)**: Van der Pol relaxation oscillator with non-conservative nonlinear damping.
12. **[`feigenbaum_bifurcation_tree.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/feigenbaum_bifurcation_tree.py)**: Logistic map period-doubling cascade, Feigenbaum universality constants $\delta$ and $\alpha$.
13. **[`fractal_box_counting_dimension.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/fractal_box_counting_dimension.py)**: Minkowski-Bouligand box-counting dimension for 2D fractal geometries.
14. **[`takens_delay_embedding.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/takens_delay_embedding.py)**: Takens' delay-coordinate phase-space reconstruction from scalar time series.
15. **[`arnold_cat_map.py`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/arnold_cat_map.py)**: Arnold's cat map chaotic automorphism on 2D torus, Lyapunov exponent $\ln((3+\sqrt{5})/2)$, and image permutation.

## Testing

All modules are verified via unit tests located in [`tests/`](file:///home/igorkan/repos/codes/algorithms/01_python/nonlinear_dynamics/tests).
Run tests via:
```bash
python3 -m unittest discover -s algorithms/01_python/nonlinear_dynamics/tests
```
