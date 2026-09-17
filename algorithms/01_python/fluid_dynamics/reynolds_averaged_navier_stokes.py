"""Reynolds-Averaged Navier-Stokes (RANS) and Boussinesq Eddy Viscosity Model.

Implements Reynolds stress closure tau_{ij}^R = 2 mu_t S_{ij} - 2/3 rho k delta_{ij}.
"""

from typing import Sequence
import numpy as np


class RANSBoussinesq:
    """RANS turbulent closure model."""

    def __init__(self, eddy_viscosity_mut: float, turbulent_ke_k: float, fluid_density: float = 1.0):
        self.mut = eddy_viscosity_mut
        self.k = turbulent_ke_k
        self.rho = fluid_density

    def reynolds_stress_tensor(self, strain_rate_tensor: Sequence[Sequence[float]]) -> np.ndarray:
        """tau_{ij}^R = 2 mu_t S_{ij} - 2/3 rho k delta_{ij}."""
        s = np.array(strain_rate_tensor, dtype=np.float64)
        return 2.0 * self.mut * s - (2.0 / 3.0) * self.rho * self.k * np.eye(3)
