"""Hartree-Fock Self-Consistent Field (SCF) for Helium Two-Electron Atom."""


def helium_scf_energy(zeta: float, Z: float = 2.0) -> float:
    """Helium ground state energy E(zeta) = zeta^2 - 2*Z*zeta + (5/8)*zeta."""
    return float(zeta**2 - 2.0 * Z * zeta + (5.0 / 8.0) * zeta)


def optimal_helium_effective_charge(Z: float = 2.0) -> float:
    """Optimal zeta = Z - 5/16."""
    return float(Z - 5.0 / 16.0)
