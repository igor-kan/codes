"""
Multipole Expansion of Electrostatic Charge Distributions.
References: Arfken, Weber, Harris - Mathematical Methods for Physicists.
"""
import numpy as np

def multipole_moments(charges: list, positions: list):
    """
    Compute total charge Q, dipole vector p, and quadrupole tensor Q_ij:
    Q_ij = sum q_k (3 r_i r_j - delta_ij r^2)
    """
    charges = np.asarray(charges, dtype=float)
    positions = np.asarray(positions, dtype=float)

    total_charge = np.sum(charges)
    dipole = np.sum(charges[:, None] * positions, axis=0)

    quadrupole = np.zeros((3, 3))
    for q, r in zip(charges, positions):
        r2 = np.dot(r, r)
        quadrupole += q * (3.0 * np.outer(r, r) - r2 * np.eye(3))

    return total_charge, dipole, quadrupole
