# Computational Fluid & Magnetohydrodynamics (MHD) Package

A modern scientific suite of computational fluid dynamics, plasma physics, and magnetohydrodynamics algorithms inspired by Landau & Lifshitz Vol 8 (*Electrodynamics of Continuous Media*), Schorghofer (*Lessons in Scientific Computing*), and Turner (*Applied Scientific Computing in Python*).

## Modules
1. **alfven_wave_dispersion.py**: Ideal MHD Alfvén, fast, and slow magnetosonic dispersion.
2. **magnetic_induction_equation.py**: Resistive magnetic induction, magnetic Reynolds number, and diffusion.
3. **parker_solar_wind.py**: Parker transonic solar wind critical sonic radius and Mach profile.
4. **hartmann_conducting_flow.py**: Hartmann conducting channel flow with transverse magnetic field.
5. **tearing_mode_reconnection.py**: Sweet-Parker and FKR resistive tearing mode reconnection scalings.
6. **alpha_omega_dynamo.py**: Mean-field kinematic solar dynamo alpha-omega cycle and dynamo waves.
7. **grad_shafranov_solver.py**: Grad-Shafranov toroidal plasma equilibrium and Solov'ev flux surfaces.
8. **bohm_classical_diffusion.py**: Classical collisional cross-field transport vs. Bohm diffusion.
9. **couette_cylinder_stability.py**: Rayleigh centrifugal stability of concentric rotating cylinders.
10. **blast_wave_sedov_von_neumann.py**: Sedov self-similar strong blast wave shock front evolution.
11. **kelvin_helmholtz_mhd.py**: Magnetized Kelvin-Helmholtz shear flow interface stability.
12. **rayleigh_buoyancy_interface_mhd.py**: Magnetized Rayleigh interface buoyancy interface buoyancy instability.
13. **debye_shielding_sheath.py**: Plasma Debye length, electron plasma frequency, and Bohm sheath velocity.
14. **vortex_sheet_birkhoff_rott.py**: Birkhoff-Rott vortex sheet roll-up with Krasny regularization.
15. **shallow_water_1d_riemann.py**: 1D nonlinear shallow water (Saint-Venant) Roe Riemann solver.

## Testing
Run unit tests with pytest:
```bash
pytest algorithms/01_python/computational_fluid_and_mhd/
```
