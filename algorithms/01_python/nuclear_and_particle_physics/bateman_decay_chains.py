"""
Bateman Equations for Radioactive Decay Chains.
References: Kenneth S. Krane - Introductory Nuclear Physics (Ch. 6).
"""
import numpy as np

def bateman_activity_chain(t: float, half_lives: list, n0: float = 1.0) -> list:
    """
    Calculate population N_i(t) in sequential radioactive decay chain 1 -> 2 -> ... -> k.
    """
    lambdas = [np.log(2.0) / t_half for t_half in half_lives]
    k = len(lambdas)
    N = []

    for i in range(k):
        Ni = 0.0
        for j in range(i + 1):
            denom = 1.0
            for p in range(i + 1):
                if p != j:
                    denom *= (lambdas[p] - lambdas[j])
            c_j = 1.0 / denom if denom != 0 else 0.0
            Ni += c_j * np.exp(-lambdas[j] * t)
        for m in range(i):
            Ni *= lambdas[m]
        N.append(float(n0 * Ni))

    return N
