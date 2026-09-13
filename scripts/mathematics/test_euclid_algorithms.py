#!/usr/bin/env python3
"""
Test suite for Euclidean algorithms and numerical variants.
Verifies equivalence between subtractive, modulo, binary, extended, and Gaussian algorithms.
"""

import math
import sys
from typing import Tuple, List

def gcd_subtractive(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0: return b
    if b == 0: return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def gcd_euclidean(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t

def gcd_binary(u: int, v: int) -> int:
    u, v = abs(u), abs(v)
    if u == 0: return v
    if v == 0: return u
    shift = 0
    while ((u | v) & 1) == 0:
        u >>= 1
        v >>= 1
        shift += 1
    while (u & 1) == 0:
        u >>= 1
    while v != 0:
        while (v & 1) == 0:
            v >>= 1
        if u > v:
            u, v = v, u
        v -= u
    return u << shift

def mod_inverse(a: int, m: int) -> int:
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return (x % m + m) % m

def gcd_gaussian(alpha: complex, beta: complex) -> complex:
    while abs(beta) > 1e-9:
        q_complex = alpha / beta
        q = complex(round(q_complex.real), round(q_complex.imag))
        alpha, beta = beta, alpha - q * beta
    return alpha

def continued_fraction(a: int, b: int) -> List[int]:
    coeffs = []
    while b != 0:
        q = a // b
        coeffs.append(q)
        a, b = b, a - q * b
    return coeffs

def run_tests():
    test_cases = [
        (48, 18),
        (101, 10),
        (1071, 462),
        (55, 34),       # Consecutive Fibonacci numbers (Lamé worst-case)
        (252, 105),
        (123456, 7890),
        (999983, 999979), # Twin primes
        (0, 42),
        (42, 0),
        (1, 1000),
    ]

    print("=== Running Euclidean Algorithm Validation Suite ===")
    for a, b in test_cases:
        expected = math.gcd(a, b)
        
        # Test Modulo
        g_mod = gcd_euclidean(a, b)
        assert g_mod == expected, f"Modulo failed for ({a}, {b}): {g_mod} != {expected}"
        
        # Test Binary
        g_bin = gcd_binary(a, b)
        assert g_bin == expected, f"Binary failed for ({a}, {b}): {g_bin} != {expected}"
        
        # Test Subtractive (skip if too large to prevent timeout)
        if max(a, b) <= 10000:
            g_sub = gcd_subtractive(a, b)
            assert g_sub == expected, f"Subtractive failed for ({a}, {b}): {g_sub} != {expected}"
            
        # Test Extended GCD
        g_ext, x, y = extended_gcd(a, b)
        assert g_ext == expected, f"Extended GCD value failed for ({a}, {b})"
        assert a * x + b * y == expected, f"Bézout identity failed: {a}*{x} + {b}*{y} != {expected}"
        
        # Test Continued Fraction reconstruction (for positive b)
        if b > 0:
            cf = continued_fraction(a, b)
            # reconstruct fraction from CF
            num, den = 1, 0
            for q in reversed(cf):
                num, den = q * num + den, num
            reconstructed_gcd = math.gcd(num, den)
            assert num // reconstructed_gcd == a // expected, f"CF failed for ({a}, {b})"
            assert den // reconstructed_gcd == b // expected, f"CF failed for ({a}, {b})"
            
        print(f"  ✓ Validated pair ({a}, {b}): gcd = {expected}")

    # Test Modular Inverse
    print("\n=== Testing Modular Inverse ===")
    assert (17 * mod_inverse(17, 3120)) % 3120 == 1
    assert (3 * mod_inverse(3, 11)) % 11 == 1
    print("  ✓ Modular inverses verified.")

    # Test Gaussian GCD
    print("\n=== Testing Gaussian Integers Z[i] GCD ===")
    # (1 + 3i) and (3 + i) share factor (1 + i) since 1+3i = (1+i)(2+i)
    g_gauss = gcd_gaussian(1 + 3j, 3 + 1j)
    norm = round(abs(g_gauss)**2)
    assert norm == 2 or norm == 10, f"Gaussian GCD unexpected norm: {norm}"
    print(f"  ✓ Gaussian GCD(1+3i, 3+i) = {g_gauss} (norm = {norm})")

    print("\n🎉 ALL EUCLIDEAN ALGORITHM TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
