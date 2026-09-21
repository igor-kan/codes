"""
Cramer-Chernoff Large Deviation Bound and Legendre-Fenchel Transform.
Reference: Evans & Rosenthal, Probability and Statistics.
"""
import numpy as np

def bernoulli_chernoff_bound(p: float, a: float, n: int) -> float:
    """
    P(S_n >= n a) <= exp(-n D(a || p)) for a > p.
    D(a || p) = a ln(a/p) + (1-a) ln((1-a)/(1-p)).
    """
    if a <= p:
        return 1.0
    kl = a * np.log(a / p) + (1.0 - a) * np.log((1.0 - a) / (1.0 - p))
    return float(np.exp(-n * kl))
