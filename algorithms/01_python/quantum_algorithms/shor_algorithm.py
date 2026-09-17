"""Shor's Quantum Factorization Algorithm and Order Finding.

Finds non-trivial factors of composite integer N = p * q via order finding a^r = 1 mod N.
"""

import math
from typing import Tuple, Optional
import numpy as np


class ShorAlgorithm:
    """Order finding and factorization algorithm."""

    @staticmethod
    def find_order_classical(a: int, n: int) -> int:
        """Find smallest r >= 1 such that a^r = 1 mod N."""
        if math.gcd(a, n) != 1:
            return 0
        r = 1
        curr = a % n
        while curr != 1:
            curr = (curr * a) % n
            r += 1
        return r

    @classmethod
    def factorize(cls, n: int, seed_a: Optional[int] = None) -> Tuple[int, int]:
        """Factorize N using order finding."""
        if n % 2 == 0:
            return 2, n // 2
        for a in range(2, n):
            if seed_a and a != seed_a:
                continue
            g = math.gcd(a, n)
            if g > 1:
                return g, n // g
            r = cls.find_order_classical(a, n)
            if r % 2 == 0:
                p1 = math.gcd(pow(a, r // 2, n) - 1, n)
                p2 = math.gcd(pow(a, r // 2, n) + 1, n)
                if 1 < p1 < n:
                    return p1, n // p1
                if 1 < p2 < n:
                    return p2, n // p2
        raise RuntimeError("Factorization failed to find split")
