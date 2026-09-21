"""
Nuclear Reaction Q-Value and Exothermicity.
References: Kenneth S. Krane - Introductory Nuclear Physics (Ch. 11).
"""
import numpy as np

def reaction_q_value(masses_reactants_amu: list, masses_products_amu: list) -> float:
    """Q = (sum M_reactants - sum M_products) * 931.494 MeV."""
    dM = sum(masses_reactants_amu) - sum(masses_products_amu)
    return float(dM * 931.494)
