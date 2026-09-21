# Modern Scientific Fortran 2018 Suite

A comprehensive collection of 15 numerical and computational physics algorithms implemented in Modern Fortran 2018, leveraging `iso_fortran_env`, pure/elemental procedures, explicit interfaces, and strong type safety.

Reference text: Ray, *Fortran 2018 with Parallel Programming* (2020); Fatica & Ruetsch, *CUDA Fortran for Scientists and Engineers* (2014).

## Algorithms Included
1. **rk4_integrator.f90**: 4th-order Runge-Kutta ODE integrator with procedure interfaces.
2. **radix2_fft.f90**: Cooley-Tukey radix-2 Fast Fourier Transform with in-place bit reversal.
3. **thomas_tridiagonal.f90**: Thomas algorithm (TDMA) for $O(N)$ tridiagonal linear systems.
4. **simpson_quadrature.f90**: Composite Simpson's 1/3 rule numerical quadrature.
5. **conjugate_gradient.f90**: Linear Conjugate Gradient solver for symmetric positive-definite systems.
6. **matrix_coarray_ops.f90**: High-performance pure matrix and vector operations.
7. **monte_carlo_integration.f90**: Multi-dimensional Monte Carlo integration with standard error bounds.
8. **lu_decomposition.f90**: LU decomposition with partial row pivoting and substitution.
9. **cubic_spline.f90**: Natural cubic spline interpolation with continuous 2nd derivatives.
10. **bisection_root.f90**: Robust bisection root-finding method.
11. **cholesky_factorization.f90**: Cholesky $L L^T$ decomposition for positive-definite matrices.
12. **gram_schmidt_qr.f90**: Modified Gram-Schmidt QR decomposition.
13. **golden_section_search.f90**: Golden section 1D unimodal function minimizer.
14. **heat_equation_explicit.f90**: 1D transient heat diffusion with FTCS finite differences.
15. **polynomial_roots_companion.f90**: Horner polynomial evaluation and Newton-Raphson root finder.

## Compilation & Testing
```bash
make test
```
