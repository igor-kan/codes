"""Watson's Lemma for Asymptotic Expansions of Laplace-Type Integrals."""
import numpy as np
from scipy.special import gamma


def watson_lemma_leading_term(alpha: float, c0: float, lam: float) -> float:
    """Integral_0^infty t^alpha * c0 * exp(-lambda * t) dt = c0 * Gamma(alpha + 1) / lambda^(alpha + 1)."""
    return float(c0 * gamma(alpha + 1.0) / (lam**(alpha + 1.0)))
