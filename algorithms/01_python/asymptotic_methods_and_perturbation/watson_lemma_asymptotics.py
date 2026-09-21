"""
Watson's Lemma for Asymptotics of Laplace-Type Integrals:
I(s) = int_0^infty e^{-s t} t^lambda f(t) dt as s -> infty.
Reference: Mauch, Intro to Applied Mathematics, Ch. 27; Chow.
"""
from scipy.special import gamma

def watson_leading_term(lambda_val: float, a0: float, s: float) -> float:
    """I(s) approx a0 * Gamma(lambda + 1) / s^{lambda + 1}."""
    return float(a0 * gamma(lambda_val + 1.0) / (s**(lambda_val + 1.0)))
