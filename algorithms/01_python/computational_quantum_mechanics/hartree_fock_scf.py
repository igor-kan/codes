"""
Hartree-Fock Self-Consistent Field (SCF) for Helium Ground State.
References: Izaac & Wang - Computational Quantum Mechanics (Ch. 6).
"""
import numpy as np

def helium_hartree_fock_energy(alpha_opt: float = 1.6875, Z: float = 2.0) -> float:
    """
    Variational Hartree-Fock ground state energy for Helium with 1s orbital psi(r) = sqrt(alpha^3/pi) e^{-alpha r}.
    E(alpha) = alpha^2 - 2 Z alpha + (5/8) alpha
    Optimal alpha = Z - 5/16 = 2 - 0.3125 = 1.6875
    E_min = -(Z - 5/16)^2 in Rydbergs or atomic units = -2.84765625 Hartree
    """
    kinetic = alpha_opt**2
    electron_nuclear = -2.0 * Z * alpha_opt
    electron_electron = (5.0 / 8.0) * alpha_opt
    return kinetic + electron_nuclear + electron_electron
