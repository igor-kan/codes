# Computational Optics & Fourier Acoustics Package

A comprehensive library of wave optics, Fourier acoustics, and electromagnetic polarization algorithms inspired by Born & Wolf, Boas, Arfken, and Blennow.

## Modules
1. **fresnel_diffraction_integral.py**: Angular spectrum / transfer function Fresnel wave propagation.
2. **fraunhofer_airy_pattern.py**: Circular aperture Airy disk diffraction pattern and Rayleigh limit.
3. **zernike_polynomials.py**: Zernike circular wavefront aberration polynomials (defocus, astigmatism, coma).
4. **transfer_matrix_thin_films.py**: Abelès characteristic matrix method for multilayer thin-film coatings.
5. **ray_transfer_abcd.py**: ABCD 2x2 ray transfer matrix and Gaussian beam q-parameter propagation.
6. **fresnel_equations_polarization.py**: Fresnel coefficients for TE/TM polarization, Brewster, and TIR.
7. **coherence_michelson_interferometer.py**: Temporal coherence, fringe visibility, and Wiener-Khinchin theorem.
8. **helmholtz_acoustic_resonator.py**: Helmholtz acoustic resonator resonance frequency with end correction.
9. **bessel_beam_propagation.py**: Non-diffracting zero-order Bessel beam and axicon optics.
10. **jones_calculus_polarization.py**: Jones vectors and matrices for polarizers and waveplates.
11. **mueller_stokes_formalism.py**: Stokes vectors, degree of polarization, and Mueller matrices.
12. **talbot_self_imaging.py**: Talbot near-field grating self-imaging and fractional Talbot distance.
13. **spatial_filter_pinhole.py**: Fourier 4f optical spatial filtering and optimum pinhole design.
14. **acoustic_doppler_relativity.py**: Classical acoustic and relativistic optical Doppler frequency shifts.
15. **acousto_optic_bragg_diffraction.py**: Acousto-optic modulator (AOM) Bragg diffraction and efficiency.

## Testing
Run unit tests with pytest:
```bash
pytest algorithms/01_python/computational_optics_and_fourier_acoustics/
```
