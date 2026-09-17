# Geophysics, Seismology & Geodynamics

A comprehensive Python suite of algorithms for solid Earth geophysics, seismic wave propagation, earthquake statistics and source mechanics, gravity and magnetic fields, lithospheric heat flow, and mantle dynamics.

## Modules

1. **[`seismic_wave_speeds.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/seismic_wave_speeds.py)**: Elastic P-wave velocity $v_p$, S-wave velocity $v_s$, and Poisson's ratio $\nu$.
2. **[`snells_law_seismic_refraction.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/snells_law_seismic_refraction.py)**: Snell's law critical refraction, head wave travel-time intercept curves, and crossover distance.
3. **[`seismic_reflection_nmo.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/seismic_reflection_nmo.py)**: Hyperbolic reflection travel time $t^2(x) = t_0^2 + x^2 / v_{\text{rms}}^2$ and Normal Moveout (NMO) correction.
4. **[`earthquake_moment_magnitude.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/earthquake_moment_magnitude.py)**: Fault scalar seismic moment $M_0 = \mu A \bar{D}$ and Hanks-Kanamori moment magnitude scale $M_w$.
5. **[`gutenberg_richter_law.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/gutenberg_richter_law.py)**: Gutenberg-Richter frequency-magnitude relation $\log_{10} N = a - b M$ and Aki-Utsu maximum-likelihood $b$-value estimation.
6. **[`omori_aftershock_law.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/omori_aftershock_law.py)**: Modified Omori law for aftershock decay rate $n(t) = K / (t + c)^p$ and cumulative event count.
7. **[`airy_pratt_isostasy.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/airy_pratt_isostasy.py)**: Airy-Heiskanen crustal root compensation $r = h \rho_c / (\rho_m - \rho_c)$ and Pratt-Hayford variable density crustal columns.
8. **[`gravitational_bouguer_anomaly.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/gravitational_bouguer_anomaly.py)**: Free-air correction, Bouguer infinite slab plate correction $\Delta g_{\text{BP}} = 2\pi G \rho h$, and complete Bouguer gravity anomaly.
9. **[`geomagnetic_dipole_field.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/geomagnetic_dipole_field.py)**: Geocentric magnetic dipole field vectors ($B_r$, $B_\theta$), total intensity, and magnetic inclination $\tan I = 2 \tan\lambda$.
10. **[`heat_flow_geotherm.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/heat_flow_geotherm.py)**: Continental 1D steady-state conductive geotherm with radiogenic heat production $A$.
11. **[`oceanic_crust_cooling_halfspace.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/oceanic_crust_cooling_halfspace.py)**: Thermal boundary layer half-space cooling model $T(z, t)$ and seafloor bathymetric subsidence $d(t) \propto \sqrt{t}$.
12. **[`chandler_wobble_euler.py`](file:///home/igorkan/repos/codes/algorithms/01_python/chandler_wobble_euler.py)**: Rigid Euler free precession period ($\approx 305$ days) and elastic Chandler wobble period ($\approx 433$ days).
13. **[`rayleigh_love_surface_waves.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/rayleigh_love_surface_waves.py)**: Rayleigh wave nondispersive halfspace phase velocity $v_R / v_s \approx (0.87 + 1.12\nu) / (1 + \nu)$.
14. **[`focal_mechanism_beachball.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/focal_mechanism_beachball.py)**: Strike, dip, and rake to fault normal and slip vectors in North-East-Down frames, double-couple P-wave radiation patterns.
15. **[`mantle_convection_rayleigh_benard.py`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/mantle_convection_rayleigh_benard.py)**: Rayleigh number $\text{Ra} = (\rho g \alpha \Delta T d^3) / (\kappa \eta)$ and convective onset thresholds.

## Testing

All modules are verified via unit tests located in [`tests/`](file:///home/igorkan/repos/codes/algorithms/01_python/geophysics/tests).
Run tests via:
```bash
python3 -m unittest discover -s algorithms/01_python/geophysics/tests
```
