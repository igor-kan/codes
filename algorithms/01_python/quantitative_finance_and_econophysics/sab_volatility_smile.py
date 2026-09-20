"""
SABR Model Implied Volatility Formula (Hagan et al.).
References: Jovanovic - Econophysics and Financial Economics.
"""
import numpy as np

def sabr_implied_volatility(F: float, K: float, T: float, alpha: float, beta: float, rho: float, nu: float) -> float:
    """Hagan et al. asymptotic implied volatility formula for SABR model."""
    if F == K:
        f_mid = F**(1.0 - beta)
        term1 = alpha / f_mid
        term2 = 1.0 + (((1.0 - beta)**2 / 24.0) * (alpha**2 / (F**(2.0 - 2.0 * beta))) +
                       (rho * beta * nu * alpha / (4.0 * f_mid)) +
                       ((2.0 - 3.0 * rho**2) / 24.0) * nu**2) * T
        return float(term1 * term2)
    
    log_fk = np.log(F / K)
    f_mid = (F * K)**((1.0 - beta) / 2.0)
    z = (nu / alpha) * f_mid * log_fk
    x_z = np.log((np.sqrt(1.0 - 2.0 * rho * z + z**2) + z - rho) / (1.0 - rho))

    num = alpha * (1.0 + (((1.0 - beta)**2 / 24.0) * (alpha**2 / (f_mid**2)) +
                          (rho * beta * nu * alpha / (4.0 * f_mid)) +
                          ((2.0 - 3.0 * rho**2) / 24.0) * nu**2) * T)
    denom = f_mid * (1.0 + ((1.0 - beta)**2 / 24.0) * log_fk**2 + ((1.0 - beta)**4 / 1920.0) * log_fk**4)
    return float((num / denom) * (z / x_z))
