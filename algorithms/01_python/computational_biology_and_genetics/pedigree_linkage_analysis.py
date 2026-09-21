"""
LOD Score Calculation for Genetic Linkage Analysis in Pedigrees.
Reference: Campbell Biology (12th Ed.), Ch. 15 (The Chromosomal Basis of Inheritance); Morton (1955).
"""
import numpy as np

def lod_score(n_recombinants: int, n_non_recombinants: int, theta: float) -> float:
    """
    Z(theta) = log10 [ L(theta) / L(0.5) ]
             = log10 [ (theta^R * (1 - theta)^NR) / (0.5^(R + NR)) ]
    A LOD score >= 3.0 provides significant evidence for linkage.
    """
    r = n_recombinants
    nr = n_non_recombinants
    n_total = r + nr
    
    if theta <= 0.0 or theta >= 0.5:
        return 0.0
        
    likelihood_theta = (theta**r) * ((1.0 - theta)**nr)
    likelihood_independent = 0.5**n_total
    
    lod = np.log10(likelihood_theta / likelihood_independent)
    return float(lod)
