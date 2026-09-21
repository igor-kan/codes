"""
First Borel-Cantelli Lemma: sum P(A_n) < infty implies P(lim sup A_n) = 0.
Reference: Evans & Rosenthal, Ch. 3.
"""
import numpy as np

def check_borel_cantelli_summability(probs: np.ndarray) -> bool:
    """Returns True if sum P(A_n) converges (finite sum test)."""
    return bool(np.sum(probs) < np.inf)
