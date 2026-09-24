"""Reversible-Jump MCMC Dimension Matching Acceptance Ratio."""
import numpy as np


def rjmcmc_acceptance_probability(p_y_given_m1: float, p_y_given_m2: float,
                                  prior_ratio: float, proposal_ratio: float, jacobian_det: float) -> float:
    """alpha = min(1, likelihood_ratio * prior_ratio * proposal_ratio * |det J|)."""
    ratio = (p_y_given_m2 / p_y_given_m1) * prior_ratio * proposal_ratio * abs(jacobian_det)
    return min(1.0, float(ratio))
