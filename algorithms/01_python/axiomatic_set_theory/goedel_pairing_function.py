"""
Gödel Pairing Function: Quadratic Bijection between N x N and N.
Reference: Jech, Set Theory, Ch. 3.
"""
import math
from typing import Tuple

def goedel_pair(x: int, y: int) -> int:
    """
    Cantor / Gödel pairing: pi(x, y) = 1/2 (x + y)(x + y + 1) + y.
    """
    return ((x + y) * (x + y + 1)) // 2 + y

def goedel_unpair(z: int) -> Tuple[int, int]:
    """
    Inverse pairing function.
    """
    w = int((math.isqrt(8 * z + 1) - 1) // 2)
    t = (w * (w + 1)) // 2
    y = z - t
    x = w - y
    return x, y
