#!/usr/bin/env python3
"""
Unit Test Suite: Tensor Index Algebra, Kronecker Delta, and Dirac Delta Approximations.
"""

import numpy as np
import math

def kronecker_delta(i: int, j: int) -> int:
    return 1 if i == j else 0

def levi_civita(i: int, j: int, k: int) -> int:
    if (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        return 1
    elif (i, j, k) in [(0, 2, 1), (2, 1, 0), (1, 0, 2)]:
        return -1
    return 0

def test_kronecker_and_levi_civita():
    print("=== 1. Testing Kronecker Delta and Trace ===")
    trace_3d = sum(kronecker_delta(i, i) for i in range(3))
    assert trace_3d == 3, f"Trace failed: {trace_3d} != 3"
    print(f"  ✓ Trace in 3D: delta^i_i = {trace_3d}")

    # Sifting property
    v = [13.0, 42.0, -7.5]
    for i in range(3):
        sifted = sum(kronecker_delta(i, j) * v[j] for j in range(3))
        assert math.isclose(sifted, v[i]), f"Sifting failed for index {i}"
    print("  ✓ Kronecker delta sifting property verified.")

    print("\n=== 2. Testing Epsilon-Delta Contraction Identity ===")
    # Identity: sum_i e_ijk * e_imn = delta_jm * delta_kn - delta_jn * delta_km
    for j in range(3):
        for k in range(3):
            for m in range(3):
                for n in range(3):
                    lhs = sum(levi_civita(i, j, k) * levi_civita(i, m, n) for i in range(3))
                    rhs = kronecker_delta(j, m) * kronecker_delta(k, n) - kronecker_delta(j, n) * kronecker_delta(k, m)
                    assert lhs == rhs, f"Identity failed for (j={j}, k={k}, m={m}, n={n}): {lhs} != {rhs}"
    print("  ✓ Epsilon-delta contraction identity holds across all 81 index combinations.")

    print("\n=== 3. Testing Vector Triple Product via Index Algebra ===")
    np.random.seed(42)
    for _ in range(10):
        A = np.random.randn(3)
        B = np.random.randn(3)
        C = np.random.randn(3)

        cross_triple = np.cross(A, np.cross(B, C))
        bac_cab = B * np.dot(A, C) - C * np.dot(A, B)
        assert np.allclose(cross_triple, bac_cab), "BAC-CAB vector identity mismatch"
    print("  ✓ Vector triple product BAC-CAB verified against NumPy cross products.")

    print("\n=== 4. Testing Dirac Delta Nascent Gaussian Sifting ===")
    # f(x) = x^2 + 3x + 5, test at x0 = 2.0 (f(2) = 15)
    f = lambda x: x**2 + 3*x + 5
    x0 = 2.0
    expected_f = f(x0)

    # Numerical convolution with sharp Gaussian: (1 / sqrt(2*pi*eps^2)) * exp(-(x - x0)^2 / (2*eps^2))
    eps = 0.005
    x_grid = np.linspace(x0 - 10*eps, x0 + 10*eps, 50000)
    dx = x_grid[1] - x_grid[0]
    gaussian_kernel = (1.0 / (math.sqrt(2 * math.pi) * eps)) * np.exp(-((x_grid - x0)**2) / (2 * eps**2))
    
    integral_area = np.sum(gaussian_kernel) * dx
    integral_sifting = np.sum(gaussian_kernel * f(x_grid)) * dx

    assert math.isclose(integral_area, 1.0, rel_tol=1e-4), f"Gaussian area = {integral_area}"
    assert math.isclose(integral_sifting, expected_f, rel_tol=1e-3), f"Sifting failed: {integral_sifting} vs {expected_f}"
    print(f"  ✓ Dirac delta Gaussian limit integral = {integral_area:.6f} (conserves unit measure)")
    print(f"  ✓ Sifted value f({x0}) = {integral_sifting:.4f} (analytical = {expected_f:.4f})")

    print("\n🎉 ALL TENSOR AND DELTA ALGEBRA TESTS PASSED!")

if __name__ == "__main__":
    test_kronecker_and_levi_civita()
