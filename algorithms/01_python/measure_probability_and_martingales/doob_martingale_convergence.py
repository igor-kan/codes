"""
Doob's Martingale Convergence and Upcrossing Inequality.
Reference: Evans & Rosenthal, Probability and Statistics; Williams, Probability with Martingales.
"""
import numpy as np

def count_upcrossings(sequence: np.ndarray, a: float, b: float) -> int:
    """
    Counts the number of upcrossings of interval [a, b] by sequence X_n.
    By Doob's Upcrossing Lemma: (b - a) E[U_{a,b}] <= E[(X_N - a)^-].
    """
    upcrossings = 0
    below = False
    for x in sequence:
        if not below and x <= a:
            below = True
        elif below and x >= b:
            upcrossings += 1
            below = False
    return upcrossings
