"""Arnold's Cat Map chaotic toral automorphism."""

from typing import Tuple
import numpy as np


class ArnoldCatMap:
    """Discrete dynamical system on the 2D unit torus T^2:
    [x_{n+1}, y_{n+1}]^T = [1, 1; 1, 2] * [x_n, y_n]^T (mod 1).
    """

    @classmethod
    def step(cls, x: float, y: float) -> Tuple[float, float]:
        """Performs one iteration on unit interval [0, 1) x [0, 1)."""
        new_x = (x + y) % 1.0
        new_y = (x + 2.0 * y) % 1.0
        return float(new_x), float(new_y)

    @classmethod
    def lyapunov_exponent(cls) -> float:
        """Analytic positive Lyapunov exponent: lambda = ln((3 + sqrt(5)) / 2)."""
        eigenvalue = (3.0 + np.sqrt(5.0)) / 2.0
        return float(np.log(eigenvalue))

    @classmethod
    def transform_image(cls, image: np.ndarray) -> np.ndarray:
        """Permutes pixels of an N x N image according to Arnold's cat map."""
        n, m = image.shape[:2]
        if n != m:
            raise ValueError("Image must be square for standard Arnold's cat map.")

        transformed = np.zeros_like(image)
        for i in range(n):
            for j in range(n):
                new_i = (i + j) % n
                new_j = (i + 2 * j) % n
                transformed[new_i, new_j] = image[i, j]

        return transformed
