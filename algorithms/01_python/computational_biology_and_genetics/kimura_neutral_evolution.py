"""
Kimura Neutral Theory of Molecular Evolution: Heterozygosity and Substitution Rate.
Reference: Campbell Biology (12th Ed.), Ch. 26; Kimura (1983).
"""
def neutral_heterozygosity(N_e: float, mu: float) -> float:
    """
    Expected equilibrium heterozygosity under infinite alleles model:
    H = 4 N_e mu / (4 N_e mu + 1).
    """
    theta = 4.0 * N_e * mu
    return float(theta / (theta + 1.0))

def neutral_substitution_rate(mu: float) -> float:
    """
    Kimura rate of neutral molecular evolution equals mutation rate per generation:
    k = (2 N mu) * (1 / (2 N)) = mu.
    """
    return float(mu)
