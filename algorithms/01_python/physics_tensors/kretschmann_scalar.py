"""Kretschmann Invariant Curvature Scalar K = R^{abcd} R_{abcd}.

Used as a coordinate-independent diagnostic to identify true physical singularities.
"""

import numpy as np


class KretschmannScalar:
    """Computes Kretschmann curvature scalar."""

    @staticmethod
    def compute(r_cov: np.ndarray, inv_g: np.ndarray) -> float:
        """K = R_{abcd} R^{abcd} = R_{abcd} g^{ap} g^{bq} g^{cr} g^{ds} R_{pqrs}."""
        r_up = np.einsum('ap,bq,cr,ds,pqrs->abcd', inv_g, inv_g, inv_g, inv_g, r_cov)
        return float(np.einsum('abcd,abcd->', r_cov, r_up))

    @staticmethod
    def schwarzschild_exact(m: float, r: float, g_const: float = 1.0, c: float = 1.0) -> float:
        """K = 48 G^2 M^2 / (c^4 r^6). Finite at horizon r = 2GM/c^2."""
        return 48.0 * (g_const**2) * (m**2) / ((c**4) * (r**6))
