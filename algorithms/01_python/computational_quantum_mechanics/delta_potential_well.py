"""1D Dirac Delta Potential Well V(x) = -alpha * delta(x)."""
import numpy as np


def delta_well_bound_energy(alpha: float, mass: float = 1.0, hbar: float = 1.0) -> float:
    """Energy of single discrete bound state."""
    return float(- (mass * alpha**2) / (2.0 * hbar**2))


def delta_well_wavefunction(x: np.ndarray, alpha: float, mass: float = 1.0, hbar: float = 1.0) -> np.ndarray:
    """Normalized bound state wavefunction."""
    kappa = mass * alpha / (hbar**2)
    return np.sqrt(kappa) * np.exp(-kappa * np.abs(x))
