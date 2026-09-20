"""
MCMC Diagnostics: Gelman-Rubin R-hat and Autocorrelation Time.
References: Evans & Rosenthal - Probability and Random Processes.
"""
import numpy as np

def gelman_rubin_rhat(chains: np.ndarray) -> float:
    """
    Compute Gelman-Rubin convergence metric R-hat across m chains of length n.
    chains: shape (m, n).
    """
    m, n = chains.shape
    chain_means = np.mean(chains, axis=1)
    overall_mean = np.mean(chain_means)

    # Between-chain variance B
    B = (n / (m - 1)) * np.sum((chain_means - overall_mean)**2)
    # Within-chain variance W
    s_sq = np.var(chains, axis=1, ddof=1)
    W = np.mean(s_sq)

    # Marginal posterior variance
    var_plus = ((n - 1) / n) * W + (1.0 / n) * B
    return float(np.sqrt(var_plus / W))
