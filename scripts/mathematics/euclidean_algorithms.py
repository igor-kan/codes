"""
Euclidean Algorithm and Modern Lattice Reduction Suite.

Implements:
1. Subtractive Euclidean Algorithm (ancient Greek ratio anthyphairesis)
2. Modulo Euclidean Algorithm (standard division remainder)
3. Stein's Binary GCD (bitwise, division-free for binary hardware)
4. Extended Euclidean Algorithm (Bézout coefficients s, t such that a*s + b*t = gcd)
5. Modular Inverse Computation via EEA
6. 2D Gauss-Lagrange Lattice Reduction (shortest vector problem in Z^2)
"""

import time
import math
from typing import Tuple

def gcd_subtractive(a: int, b: int) -> int:
    """Ancient subtractive anthyphairesis (O(max(a, b)) worst-case)."""
    a, b = abs(a), abs(b)
    if a == 0: return b
    if b == 0: return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def gcd_modulo(a: int, b: int) -> int:
    """Standard division remainder algorithm (Lamé bound: <= 5 * log10(min(a, b)))."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def gcd_binary_stein(a: int, b: int) -> int:
    """Stein's algorithm (1967): replaces expensive division with bitwise shifts."""
    a, b = abs(a), abs(b)
    if a == 0: return b
    if b == 0: return a
    
    # Factor out common powers of 2
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1
        
    while (a & 1) == 0:
        a >>= 1
        
    while b != 0:
        while (b & 1) == 0:
            b >>= 1
        if a > b:
            a, b = b, a
        b = b - a
        
    return a << shift

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean Algorithm returning (gcd, s, t) such that a*s + b*t = gcd."""
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    r0, r1 = a, b
    
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
        
    return r0, s0, t0

def mod_inverse(a: int, m: int) -> int:
    """Compute modular multiplicative inverse a^(-1) mod m via Extended GCD."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Modular inverse does not exist: gcd({a}, {m}) = {g} != 1")
    return (x % m + m) % m

def gauss_lagrange_reduction(v1: Tuple[int, int], v2: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """2D Gauss-Lagrange lattice reduction (generalizes Euclid to lattices)."""
    def dot(u, v): return u[0]*v[0] + u[1]*v[1]
    def norm_sq(u): return dot(u, u)
    
    u, v = v1, v2
    if norm_sq(v) < norm_sq(u):
        u, v = v, u
        
    while True:
        mu = round(dot(v, u) / norm_sq(u))
        v = (v[0] - mu * u[0], v[1] - mu * u[1])
        if norm_sq(v) < norm_sq(u):
            u, v = v, u
        else:
            break
            
    return u, v

if __name__ == "__main__":
    print("=== EUCLIDEAN ALGORITHM SUITE ===")
    a, b = 240, 46
    g, s, t = extended_gcd(a, b)
    print(f"Extended GCD({a}, {b}) = {g} = ({a})*({s}) + ({b})*({t})")
    assert a * s + b * t == g
    
    inv = mod_inverse(17, 3120)
    print(f"17^(-1) mod 3120 = {inv} (Verify: {17 * inv % 3120})")
    assert (17 * inv) % 3120 == 1
    
    v1 = (11, 4)
    v2 = (8, 3)
    u, v = gauss_lagrange_reduction(v1, v2)
    print(f"Gauss-Lagrange Reduction of {v1}, {v2} -> Shortest basis: {u}, {v}")
