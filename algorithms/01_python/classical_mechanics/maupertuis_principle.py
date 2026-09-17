"""Maupertuis-Jacobi Principle of Least Action and Jacobi Metric Geodesics.

Implements Arnold §37: trajectories of conservative systems with fixed energy E are geodesics
of the Jacobi metric g_{ij}^{Jacobi} = 2 (E - V(q)) a_{ij}(q) on configuration space.
"""

from typing import Callable, Sequence
import numpy as np


class MaupertuisJacobiMetric:
    """Jacobi Riemannian metric g_{ij}^J = 2 (E - V(q)) g_{ij} for classical trajectories."""

    def __init__(self, energy: float, potential_func: Callable[[np.ndarray], float],
                 flat_metric: Sequence[Sequence[float]] = ((1.0, 0.0), (0.0, 1.0))):
        self.energy = energy
        self.v_func = potential_func
        self.base_g = np.array(flat_metric, dtype=np.float64)

    def conformal_factor(self, q: Sequence[float]) -> float:
        """Omega^2(q) = 2 (E - V(q)). Must be strictly positive for physical paths."""
        q_arr = np.array(q, dtype=np.float64)
        v = self.v_func(q_arr)
        kinetic = 2.0 * (self.energy - v)
        if kinetic <= 0.0:
            raise ValueError(f"Energy E={self.energy} <= V(q)={v}: classical turning point")
        return float(kinetic)

    def metric_at(self, q: Sequence[float]) -> np.ndarray:
        """g_{ij}^{Jacobi}(q) = 2 (E - V(q)) g_{ij}^{base}."""
        return self.conformal_factor(q) * self.base_g

    def jacobi_arc_length(self, q_path: Sequence[Sequence[float]]) -> float:
        """Maupertuis action integral W = int sqrt(2(E - V(q))) ds_base."""
        pts = np.array(q_path, dtype=np.float64)
        total_w = 0.0
        for i in range(len(pts) - 1):
            q_mid = 0.5 * (pts[i] + pts[i + 1])
            dq = pts[i + 1] - pts[i]
            omega = np.sqrt(self.conformal_factor(q_mid))
            ds = np.sqrt(float(dq @ self.base_g @ dq))
            total_w += omega * ds
        return total_w
