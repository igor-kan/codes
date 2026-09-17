"""Fractal Box-Counting Dimension (Minkowski-Bouligand dimension)."""

from typing import List, Tuple
import numpy as np


class BoxCountingDimension:
    """Estimates Hausdorff / box-counting dimension D_box = lim -log(N(eps)) / log(eps)."""

    @classmethod
    def compute_dimension_2d(cls, binary_image: np.ndarray, box_sizes: List[int] = None) -> float:
        """Computes box dimension of a 2D binary array (True/1 = fractal set)."""
        h, w = binary_image.shape
        min_dim = min(h, w)

        if box_sizes is None:
            # Powers of 2 up to min_dim // 2
            box_sizes = []
            s = 2
            while s <= min_dim // 2:
                box_sizes.append(s)
                s *= 2

        counts = []
        valid_sizes = []

        for size in box_sizes:
            # Count boxes of size x size that contain at least one point
            n_h = int(np.ceil(h / size))
            n_w = int(np.ceil(w / size))
            count = 0
            for i in range(n_h):
                for j in range(n_w):
                    patch = binary_image[i * size : (i + 1) * size, j * size : (j + 1) * size]
                    if np.any(patch):
                        count += 1
            if count > 0:
                counts.append(count)
                valid_sizes.append(size)

        log_eps = -np.log(np.array(valid_sizes))
        log_n = np.log(np.array(counts))

        # Linear regression slope: log(N) = -D * log(eps) + C
        coeffs = np.polyfit(-np.log(np.array(valid_sizes)), log_n, 1)
        return float(coeffs[0])
