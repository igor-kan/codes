"""
Transfinite Ordinal Arithmetic (Addition, Multiplication) for Finite and omega-Powers.
Reference: Jech, Set Theory, Ch. 2 (Ordinals).
"""
from typing import Tuple, List

class OrdinalTerm:
    """Represents omega^exp * coeff."""
    def __init__(self, exp: int, coeff: int):
        self.exp = exp
        self.coeff = coeff

def ordinal_add(alpha: List[OrdinalTerm], beta: List[OrdinalTerm]) -> List[OrdinalTerm]:
    """
    Ordinal addition alpha + beta in Cantor normal form.
    beta absorbs terms in alpha of strictly lower degree.
    """
    if not beta:
        return alpha
    highest_beta_exp = beta[0].exp
    res = [term for term in alpha if term.exp > highest_beta_exp]
    
    # Check matching exponents
    matching = [term for term in alpha if term.exp == highest_beta_exp]
    if matching:
        res.append(OrdinalTerm(highest_beta_exp, matching[0].coeff + beta[0].coeff))
        res.extend(beta[1:])
    else:
        res.extend(beta)
    return res
