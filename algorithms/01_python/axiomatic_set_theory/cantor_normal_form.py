"""
Cantor Normal Form for Ordinals alpha = omega^{beta_1} c_1 + ... + omega^{beta_k} c_k.
Reference: Jech, Set Theory, Ch. 2.
"""
from typing import List, Tuple

def format_cantor_normal_form(terms: List[Tuple[int, int]]) -> str:
    """
    Formats a list of (exponent, coefficient) tuples into human-readable string.
    """
    parts = []
    for exp, coeff in terms:
        if exp == 0:
            parts.append(str(coeff))
        elif exp == 1:
            parts.append(f"w*{coeff}" if coeff > 1 else "w")
        else:
            parts.append(f"w^{exp}*{coeff}" if coeff > 1 else f"w^{exp}")
    return " + ".join(parts) if parts else "0"
