"""
Cardinal Arithmetic in ZFC: Addition and Multiplication of Infinite Cardinals.
Reference: Jech, Set Theory, Ch. 3 (Cardinals).
"""
from typing import Union

class Cardinal:
    def __init__(self, aleph_idx: Union[int, None] = None, finite_val: Union[int, None] = None):
        self.aleph_idx = aleph_idx
        self.finite_val = finite_val

    def is_infinite(self) -> bool:
        return self.aleph_idx is not None

def cardinal_add(kappa: Cardinal, lam: Cardinal) -> Cardinal:
    """In ZFC, kappa + lambda = max(kappa, lambda) for infinite cardinals."""
    if not kappa.is_infinite() and not lam.is_infinite():
        return Cardinal(finite_val=kappa.finite_val + lam.finite_val)
    if kappa.is_infinite() and not lam.is_infinite():
        return kappa
    if not kappa.is_infinite() and lam.is_infinite():
        return lam
    return Cardinal(aleph_idx=max(kappa.aleph_idx, lam.aleph_idx))
