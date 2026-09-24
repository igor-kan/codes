"""Perturbation Theory for Anharmonic Quartic Oscillator V(x) = 0.5 x^2 + lambda * x^4."""


def anharmonic_ground_energy(lam: float) -> float:
    """Ground state energy via 2nd-order perturbation theory."""
    E0 = 0.5
    E1 = 0.75 * lam
    E2 = - (21.0 / 8.0) * (lam**2)
    return float(E0 + E1 + E2)
