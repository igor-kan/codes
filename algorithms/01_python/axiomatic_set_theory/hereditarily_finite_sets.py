"""
Hereditarily Finite Sets V_omega and Ackermann's Integer Isomorphism.
Reference: Jech, Set Theory, Ch. 1.
"""
from typing import Set

def ackermann_encode(s: Set[int]) -> int:
    """enc(s) = sum_{x in s} 2^x."""
    return sum(1 << x for x in s)

def ackermann_decode(n: int) -> Set[int]:
    """Decodes integer n into set of bit positions."""
    s = set()
    bit = 0
    while n > 0:
        if n & 1:
            s.add(bit)
        n >>= 1
        bit += 1
    return s
