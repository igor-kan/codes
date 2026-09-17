"""Ricci Tensor R_{mu nu} and Ricci Scalar Curvature R.

Contractions of the Riemann curvature tensor: R_{mu nu} = R^lambda_{mu lambda nu}, R = g^{mu nu} R_{mu nu}.
"""

import numpy as np
try:
    from .riemann_curvature_tensor import RiemannCurvatureTensor
except ImportError:
    from riemann_curvature_tensor import RiemannCurvatureTensor


class RicciCurvature:
    """Ricci curvature tensor and scalar."""

    def __init__(self, ricci_tensor: np.ndarray, inv_metric: np.ndarray):
        self.r_mu_nu = np.array(ricci_tensor, dtype=np.float64)
        self.inv_g = np.array(inv_metric, dtype=np.float64)
        self.dim = self.r_mu_nu.shape[0]
        self.scalar = float(np.einsum('mn,mn->', self.inv_g, self.r_mu_nu))

    @classmethod
    def from_riemann(cls, riemann: RiemannCurvatureTensor, inv_metric: np.ndarray) -> 'RicciCurvature':
        """Contract Riemann tensor: R_{mu nu} = R^lambda_{mu lambda nu}."""
        r_mu_nu = np.einsum('lsln->sn', riemann.data)
        return cls(r_mu_nu, inv_metric)

    @property
    def traceless_part(self) -> np.ndarray:
        """Compute trace-free Ricci tensor: S_{mu nu} = R_{mu nu} - (1/dim) R g_{mu nu}."""
        g = np.linalg.inv(self.inv_g)
        return self.r_mu_nu - (self.scalar / self.dim) * g
