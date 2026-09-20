"""
Dirac Magnetic Monopole and Wu-Yang Overlapping Patches.
References: Landau & Lifshitz; Arfken.
"""
import numpy as np

def dirac_quantization_condition(n: int, e_charge: float, hbar: float = 1.0, c: float = 1.0) -> float:
    """Dirac charge quantization condition: g_n = n * hbar * c / (2 e)."""
    return float(n * hbar * c / (2.0 * e_charge))
