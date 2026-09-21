"""
Bailey-de Prado Deflated Sharpe Ratio (DSR) Under Multiple Testing.
Reference: Bailey & Lopez de Prado (2014); Advances in Financial Machine Learning, Ch. 14.
"""
import numpy as np
from scipy.stats import norm

def deflated_sharpe_ratio(sr_observed: float, n_trials: int, var_sr_trials: float,
                          t_observations: int, skew: float = 0.0, kurt: float = 3.0) -> float:
    """
    Calculates DSR probability that observed Sharpe Ratio is false discovery.
    """
    euler_mascheroni = 0.5772156649
    # Expected maximum Sharpe ratio under null hypothesis
    z_max = (1.0 - euler_mascheroni) * norm.ppf(1.0 - 1.0 / n_trials) + euler_mascheroni * norm.ppf(1.0 - 1.0 / (n_trials * np.e))
    sr_null = np.sqrt(var_sr_trials) * z_max
    
    # Standard deviation of Sharpe ratio
    std_sr = np.sqrt((1.0 - skew * sr_observed + 0.25 * (kurt - 1.0) * sr_observed**2) / (t_observations - 1.0))
    dsr_stat = (sr_observed - sr_null) / std_sr
    return float(norm.cdf(dsr_stat))
