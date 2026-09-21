# Modern Scientific Rust Suite

A comprehensive collection of 15 numerical and scientific computing algorithms written in pure, idiomatic Rust (2021 edition) with zero external dependencies.

## Modules Included
1. **rk4.rs**: 4th-order Runge-Kutta ODE integrator with higher-order functions.
2. **fft.rs**: In-place Radix-2 Cooley-Tukey complex Fast Fourier Transform.
3. **matrix_ops.rs**: Matrix multiplication, transpose, Frobenius norm, and trace.
4. **tridiagonal.rs**: Thomas tridiagonal linear system solver $O(N)$.
5. **quadrature.rs**: Composite Simpson's 1/3 and Gauss-Legendre numerical integration.
6. **conjugate_gradient.rs**: Iterative Linear Conjugate Gradient solver for SPD systems.
7. **quaternion.rs**: 3D spatial rotation unit quaternions and SLERP.
8. **dual_numbers.rs**: Dual numbers forward-mode automatic differentiation.
9. **bisection.rs**: Robust bisection and false position root-finding.
10. **cubic_spline.rs**: Natural cubic spline interpolation.
11. **lu_decomp.rs**: LU decomposition with partial row pivoting.
12. **statistics.rs**: Mean, sample variance, covariance, and Pearson correlation.
13. **monte_carlo.rs**: Multi-dimensional Monte Carlo integration with error bounds.
14. **least_squares.rs**: Linear least-squares regression ($y = mx + b$).
15. **golden_section.rs**: Golden-section 1D unimodal function minimum optimizer.

## Testing
```bash
cargo test
```
