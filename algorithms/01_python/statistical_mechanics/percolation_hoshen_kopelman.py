"""Hoshen-Kopelman Connected Component Cluster Labeling Algorithm.

Efficient Union-Find labeling of percolation clusters on 2D lattices.
"""

from typing import Sequence
import numpy as np


class HoshenKopelman2D:
    """Hoshen-Kopelman cluster labeling on 2D binary grid."""

    @staticmethod
    def label_clusters(grid: Sequence[Sequence[int]]) -> np.ndarray:
        """Label contiguous occupied components (1s) using 4-connectivity."""
        arr = np.array(grid, dtype=int)
        rows, cols = arr.shape
        labels = np.zeros((rows, cols), dtype=int)
        parent = [0]

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                parent[rx] = ry

        next_label = 1
        for r in range(rows):
            for c in range(cols):
                if arr[r, c] == 1:
                    left = labels[r, c - 1] if c > 0 else 0
                    up = labels[r - 1, c] if r > 0 else 0

                    if left == 0 and up == 0:
                        labels[r, c] = next_label
                        parent.append(next_label)
                        next_label += 1
                    elif left > 0 and up == 0:
                        labels[r, c] = find(left)
                    elif left == 0 and up > 0:
                        labels[r, c] = find(up)
                    else:
                        union(left, up)
                        labels[r, c] = find(left)

        for r in range(rows):
            for c in range(cols):
                if labels[r, c] > 0:
                    labels[r, c] = find(labels[r, c])
        return labels
