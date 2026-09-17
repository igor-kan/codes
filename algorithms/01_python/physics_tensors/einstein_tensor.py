"""Einstein Curvature Tensor G_{mu nu} = R_{mu nu} - 1/2 R g_{mu nu}.

Central object of Einstein's General Relativity field equations.
"""

import numpy as np
try:
    from .ricci_tensor_and_scalar import RicciCurvature
except ImportError:
    from ricci_tensor_and_scalar import RicciCurvature


class EinsteinTensor:
    """Einstein tensor G_{mu nu}."""

    def __init__(self, ricci: RicciCurvature, metric: np.ndarray, lambd: float = 0.0):
        self.metric = np.array(metric, dtype=np.float64)
        self.ricci = ricci
        self.lambd = lambd  # Cosmological constant
        self.dim = self.metric.shape[0]

        self.g_tensor = (
            self.ricci.r_mu_nu -
            0.5 * self.ricci.scalar * self.metric +
            self.lambd * self.metric
        )

    @property
    def trace(self) -> float:
        """Trace of Einstein tensor: tr(G) = (1 - dim/2) R + dim * Lambda."""
        return float(np.einsum('mn,mn->', self.ricci.inv_g, self.g_tensor))
