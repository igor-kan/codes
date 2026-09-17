# Computational Astrophysics & Stellar Dynamics

A comprehensive Python suite of algorithms covering stellar interior structure, degenerate relativistic compact objects, accretion physics, gravitational wave emission, and cosmology.

## Modules

1. **[`lane_emden_equation.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/lane_emden_equation.py)**: Polytropic stellar structure solver $(1/\xi^2) d/d\xi(\xi^2 d\theta/d\xi) = -\theta^n$ via Runge-Kutta 4th order.
2. **[`chandrasekhar_mass_limit.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/chandrasekhar_mass_limit.py)**: Theoretical upper mass limit for relativistic electron degenerate white dwarfs ($M_{\text{Ch}} \approx 1.456 M_\odot$).
3. **[`tolman_oppenheimer_volkoff.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/tolman_oppenheimer_volkoff.py)**: General relativistic hydrostatic equilibrium solver for neutron star mass-radius profiles.
4. **[`eddington_luminosity.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/eddington_luminosity.py)**: Maximum radiative luminosity $L_{\text{Edd}} = 4\pi G M c / \kappa$ and Bondi-Eddington accretion rates.
5. **[`hertzsprung_russell_relations.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/hertzsprung_russell_relations.py)**: Stefan-Boltzmann stellar luminosity $L = 4\pi R^2 \sigma T_{\text{eff}}^4$ and main-sequence mass-luminosity scaling $L \propto M^{3.5}$.
6. **[`jeans_instability_collapse.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/jeans_instability_collapse.py)**: Jeans length $\lambda_J$, Jeans mass $M_J$, and gravitational free-fall collapse timescale $\tau_{\text{ff}}$.
7. **[`roche_lobe_geometry.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/roche_lobe_geometry.py)**: Eggleton analytical approximation for effective Roche lobe radius in close binaries.
8. **[`n_body_barnes_hut.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/n_body_barnes_hut.py)**: Hierarchical QuadTree Barnes-Hut algorithm for stellar cluster $O(N \log N)$ gravitational force computation.
9. **[`accretion_disk_shakura_sunyaev.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/accretion_disk_shakura_sunyaev.py)**: Geometrically thin, optically thick accretion disk temperature profile $T(r) \propto r^{-3/4}$.
10. **[`synchrotron_radiation.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/synchrotron_radiation.py)**: Ultra-relativistic synchrotron emission power and critical frequency $\nu_c$.
11. **[`gravitational_wave_inspiral_waveform.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/gravitational_wave_inspiral_waveform.py)**: Binary chirp mass $\mathcal{M}$, frequency evolution $\dot{f}_{\text{GW}}$, and leading quadrupole strain $h(t)$.
12. **[`pulsar_spindown_dipole.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/pulsar_spindown_dipole.py)**: Magnetic dipole radiation torque, characteristic age $\tau = P / (2\dot{P})$, and surface field $B_p$.
13. **[`sedov_taylor_blast_wave.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/sedov_taylor_blast_wave.py)**: Self-similar supernova blast wave expansion radius $R(t) \propto (E t^2 / \rho_0)^{1/5}$ and shock velocity.
14. **[`cosmological_distance_ladder.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/cosmological_distance_ladder.py)**: Comoving, luminosity, and angular diameter distances in flat $\Lambda$CDM cosmology.
15. **[`dark_matter_nfw_profile.py`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/dark_matter_nfw_profile.py)**: Navarro-Frenk-White (NFW) dark matter halo density profile, enclosed mass $M(r)$, and circular velocity $v_c(r)$.

## Testing

All modules are verified via unit tests located in [`tests/`](file:///home/igorkan/repos/codes/algorithms/01_python/astrophysics/tests).
Run tests via:
```bash
python3 -m unittest discover -s algorithms/01_python/astrophysics/tests
```
