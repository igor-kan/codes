# Continuum Mechanics & Theory of Elasticity Package

A comprehensive library of continuum mechanics, elasticity, and viscoelasticity algorithms inspired by Landau & Lifshitz Vol 7 (*Theory of Elasticity*) and Zeldovich (*Higher Math for Beginners*).

## Modules
1. **cauchy_stress_invariants.py**: Cauchy stress tensor invariants (I1, I2, I3), deviatoric stress, and J2/J3.
2. **green_lagrange_strain.py**: Nonlinear Green-Lagrange finite strain vs. linearized infinitesimal strain.
3. **isotropic_hooke_law.py**: 3D isotropic constitutive relations, Lamé parameters, bulk and shear moduli.
4. **airy_stress_function.py**: Airy stress function biharmonic formulations and cantilever bending.
5. **saint_venant_torsion.py**: Saint-Venant torsion of circular and elliptical shafts, torsional rigidity.
6. **rayleigh_surface_waves.py**: Rayleigh surface acoustic wave secular equation and phase velocity.
7. **love_waves_dispersion.py**: Love surface shear wave dispersion in layered media.
8. **kelvin_voigt_viscoelastic.py**: Kelvin-Voigt parallel spring-dashpot creep compliance and dynamic modulus.
9. **maxwell_viscoelastic.py**: Maxwell series spring-dashpot stress relaxation and Deborah number.
10. **mohr_circle_3d.py**: 3D Mohr's circles, maximum shear stress, and octahedral stress state.
11. **timoshenko_beam_deflection.py**: Timoshenko deep beam theory with shear deformation corrections.
12. **von_mises_yield.py**: Von Mises and Tresca yield criteria and safety factors.
13. **griffith_fracture_energy.py**: Griffith brittle crack propagation energy release and stress intensity factors.
14. **hertzian_contact_mechanics.py**: Hertzian elastic spherical contact pressure and indentation.
15. **cylindrical_thick_pipe_lame.py**: Lamé thick-walled pressure vessel stress distribution.

## Testing
Run unit tests with pytest:
```bash
pytest algorithms/01_python/continuum_mechanics_and_elasticity/
```
