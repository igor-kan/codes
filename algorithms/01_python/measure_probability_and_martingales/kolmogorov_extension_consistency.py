"""
Kolmogorov Extension Consistency Condition Checker for Transition Semigroups.
Reference: Evans & Rosenthal; Billingsley, Probability and Measure.
"""
import numpy as np

def check_chapman_kolmogorov(P_s: np.ndarray, P_t: np.ndarray, P_st: np.ndarray) -> bool:
    """Verifies Chapman-Kolmogorov semigroup property: P(s + t) = P(s) P(t)."""
    return bool(np.allclose(P_s @ P_t, P_st, atol=1e-8))
