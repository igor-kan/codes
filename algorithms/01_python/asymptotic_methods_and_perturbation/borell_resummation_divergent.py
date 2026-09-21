"""
Borel Transform of Factorially Divergent Perturbation Series sum c_n n! z^n:
B(t) = sum c_n t^n.
Reference: Mauch; Zinn-Justin, Quantum Field Theory and Critical Phenomena.
"""
import numpy as np

def borel_transform_geometric(t: float, c0: float = 1.0) -> float:
    """For Euler series sum (-1)^n n! z^n, Borel transform is 1 / (1 + t)."""
    return float(c0 / (1.0 + t))
