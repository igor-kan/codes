"""Jarzynski Equality: <exp(- beta W)> = exp(- beta Delta F).

Reconstructs equilibrium free energy differences from non-equilibrium work distributions.
"""

from typing import Sequence
import numpy as np


class JarzynskiEquality:
    """Non-equilibrium work relation estimator."""

    @staticmethod
    def free_energy_difference(work_trajectories: Sequence[float], beta: float) -> float:
        """Delta F = - 1/beta ln <exp(-beta W)>."""
        w = np.array(work_trajectories, dtype=np.float64)
        avg_exp = np.mean(np.exp(-beta * w))
        return float(- np.log(avg_exp) / beta)
