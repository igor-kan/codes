"""K-Means Clustering from First Principles.

Implements iterative Lloyd's algorithm with Euclidean distance metric
and convergence detection.
"""

import math
import random
from typing import List, Tuple

Point = Tuple[float, ...]

def euclidean_dist(p1: Point, p2: Point) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def kmeans(points: List[Point], k: int, max_iter: int = 100, tol: float = 1e-6) -> Tuple[List[Point], List[int]]:
    if k <= 0 or not points:
        return [], []

    # Initialize centroids deterministically for reproducibility
    random.seed(42)
    centroids = random.sample(points, min(k, len(points)))
    dim = len(points[0])

    labels = [0] * len(points)

    for iteration in range(max_iter):
        # Assignment step
        new_labels = []
        for p in points:
            dists = [euclidean_dist(p, c) for c in centroids]
            new_labels.append(dists.index(min(dists)))

        # Update step
        new_centroids: List[Point] = []
        max_shift = 0.0

        for cluster_idx in range(k):
            cluster_pts = [points[i] for i, lbl in enumerate(new_labels) if lbl == cluster_idx]
            if not cluster_pts:
                new_centroids.append(centroids[cluster_idx])
                continue

            mean_pt = tuple(sum(p[d] for p in cluster_pts) / len(cluster_pts) for d in range(dim))
            shift = euclidean_dist(centroids[cluster_idx], mean_pt)
            max_shift = max(max_shift, shift)
            new_centroids.append(mean_pt)

        centroids = new_centroids
        labels = new_labels

        if max_shift < tol:
            break

    return centroids, labels

if __name__ == "__main__":
    # 2 clusters: around (1, 1) and (10, 10)
    data = [
        (0.9, 1.1), (1.0, 0.9), (1.2, 1.0), (0.8, 1.2),
        (9.8, 10.1), (10.1, 9.9), (10.0, 10.2), (9.9, 9.8)
    ]
    centroids, labels = kmeans(data, k=2)
    assert len(centroids) == 2
    # Cluster labels for first 4 points must be equal, and last 4 points equal
    assert labels[0] == labels[1] == labels[2] == labels[3]
    assert labels[4] == labels[5] == labels[6] == labels[7]
    assert labels[0] != labels[4]

    print(f"[Python ML] K-Means clustered {len(data)} points into 2 distinct components.")
