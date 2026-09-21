"""
Bethe-Weizsäcker Semi-Empirical Mass Formula (SEMF).
References: Kenneth S. Krane - Introductory Nuclear Physics (Ch. 3).
"""
import numpy as np

def nuclear_binding_energy(Z: int, A: int) -> float:
    """
    Binding energy B(A, Z) = a_v A - a_s A^(2/3) - a_c Z(Z-1) A^(-1/3) - a_a (A - 2Z)^2 A^(-1) + delta(A, Z).
    Parameters in MeV: a_v=15.8, a_s=18.3, a_c=0.714, a_a=23.2, a_p=12.0.
    """
    N = A - Z
    if A <= 0 or Z < 0:
        return 0.0

    av = 15.8
    asurf = 18.3
    ac = 0.714
    aa = 23.2
    ap = 12.0

    vol = av * A
    surf = asurf * (A**(2.0 / 3.0))
    coulomb = ac * Z * (Z - 1) / (A**(1.0 / 3.0))
    asym = aa * ((A - 2 * Z)**2) / A

    # Pairing term
    if A % 2 != 0:
        delta = 0.0
    elif Z % 2 == 0:
        delta = ap / np.sqrt(A)  # even-even
    else:
        delta = -ap / np.sqrt(A)  # odd-odd

    return float(vol - surf - coulomb - asym + delta)

def binding_energy_per_nucleon(Z: int, A: int) -> float:
    """B / A in MeV."""
    return float(nuclear_binding_energy(Z, A) / A)
