# Plasma Physics & Magnetohydrodynamics (MHD)

A comprehensive Python suite implementing kinetic theory, plasma wave dispersion relations, guiding-center drifts, magnetic confinement, and numerical MHD solvers.

## Modules

1. **[`plasma_frequency.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/plasma_frequency.py)**: Electron and ion fundamental plasma frequencies, dielectric permittivity functions $\epsilon(\omega)$.
2. **[`debye_shielding.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/debye_shielding.py)**: Debye length $\lambda_D$, plasma parameter $N_D$, screened Coulomb (Yukawa) potential calculations.
3. **[`cyclotron_gyrofrequency.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/cyclotron_gyrofrequency.py)**: Relativistic and non-relativistic gyrofrequencies, Larmor radii, and magnetic moment $\mu$.
4. **[`guiding_center_drifts.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/guiding_center_drifts.py)**: $\mathbf{E} \times \mathbf{B}$ drift, $\nabla B$ grad-B drift, curvature drift, and gravitational drift vectors.
5. **[`magnetic_mirror_adiabatic.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/magnetic_mirror_adiabatic.py)**: Mirror ratio, loss cone angle $\alpha_{\text{loss}}$, and adiabatic trapping conditions.
6. **[`alfven_waves.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/alfven_waves.py)**: Shear Alfvén speed $v_A = B / \sqrt{\mu_0 \rho}$ and dispersion relation $\omega = v_A k_\parallel$.
7. **[`magnetosonic_waves.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/magnetosonic_waves.py)**: Fast and slow magnetosonic phase velocities across arbitrary propagation angles $\theta$.
8. **[`two_stream_instability.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/two_stream_instability.py)**: Electrostatic two-stream instability dispersion relations and maximum growth rate $\gamma_{\text{max}}$.
9. **[`landau_damping.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/landau_damping.py)**: Collisionless wave-particle Landau damping rate for thermal Maxwellian electron distributions.
10. **[`vlasov_maxwell_1d.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/vlasov_maxwell_1d.py)**: 1D1V collisionless Vlasov-Poisson phase-space distribution solver.
11. **[`pic_particle_in_cell_1d.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/pic_particle_in_cell_1d.py)**: 1D Particle-In-Cell (PIC) simulation engine with cloud-in-cell charge deposition and leapfrog integration.
12. **[`mhd_equilibrium_pinch.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/mhd_equilibrium_pinch.py)**: Bennett pinch equilibrium relation and radial magnetic pressure balance.
13. **[`grad_shafranov_solver.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/grad_shafranov_solver.py)**: 2D axisymmetric toroidal equilibrium solver for tokamak poloidal flux $\psi(R, Z)$.
14. **[`magnetic_reconnection_sweet_parker.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/magnetic_reconnection_sweet_parker.py)**: Sweet-Parker reconnection rate, Lundquist number $S$, and current sheet thickness $\delta$.
15. **[`collisionless_shock_rankine.py`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/collisionless_shock_rankine.py)**: Perpendicular MHD Rankine-Hugoniot jump conditions and shock compression ratios.

## Testing

All modules are accompanied by unit tests located in [`tests/`](file:///home/igorkan/repos/codes/algorithms/01_python/plasma_physics/tests).
Run tests via:
```bash
python3 -m unittest discover -s algorithms/01_python/plasma_physics/tests
```
