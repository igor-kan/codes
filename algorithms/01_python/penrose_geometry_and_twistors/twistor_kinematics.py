"""
Penrose Twistor representation of massless particles with spin/helicity.
Reference: Penrose, The Road to Reality, Ch. 33 (Twistor theory).
"""
import numpy as np

class Twistor:
    """
    A Penrose twistor Z^alpha = (omega^A, pi_{A'}) in C^4.
    """
    def __init__(self, omega: np.ndarray, pi_prime: np.ndarray):
        self.omega = np.asarray(omega, dtype=complex)
        self.pi_prime = np.asarray(pi_prime, dtype=complex)

    def helicity(self) -> float:
        """
        Calculates the twistor helicity s = 1/2 (omega^A bar{pi}_A + pi_{A'} bar{omega}^{A'}).
        s = 1/2 Z^alpha bar{Z}_alpha.
        """
        s = 0.5 * (np.vdot(self.pi_prime, self.omega) + np.vdot(self.omega, self.pi_prime)).real
        return float(s)

    def is_null(self) -> bool:
        """A twistor is null (helicity s = 0) if it corresponds to a classical null ray."""
        return np.isclose(self.helicity(), 0.0, atol=1e-10)
