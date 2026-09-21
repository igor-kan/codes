"""
UPGMA (Unweighted Pair Group Method with Arithmetic Mean) Distance Clustering.
Reference: Campbell Biology (12th Ed.), Ch. 26 (Phylogeny and the Tree of Life).
"""
import numpy as np
from typing import List, Tuple

def upgma_step(D: np.ndarray, clusters: List[List[int]]) -> Tuple[np.ndarray, List[List[int]], Tuple[int, int], float]:
    """Performs a single step of hierarchical UPGMA distance clustering."""
    n = len(clusters)
    min_dist = np.inf
    best_pair = (-1, -1)
    
    for i in range(n):
        for j in range(i + 1, n):
            if D[i, j] < min_dist:
                min_dist = D[i, j]
                best_pair = (i, j)
                
    i, j = best_pair
    # Merge clusters i and j
    c_new = clusters[i] + clusters[j]
    new_clusters = [clusters[k] for k in range(n) if k != i and k != j]
    new_clusters.append(c_new)
    
    # Update distance matrix
    m = len(new_clusters)
    D_new = np.zeros((m, m))
    idx_map = [k for k in range(n) if k != i and k != j]
    
    for a in range(m - 1):
        orig_a = idx_map[a]
        for b in range(a + 1, m - 1):
            orig_b = idx_map[b]
            D_new[a, b] = D_new[b, a] = D[orig_a, orig_b]
            
        # Distance between cluster a and merged cluster (i, j)
        size_i = len(clusters[i])
        size_j = len(clusters[j])
        dist_merged = (size_i * D[orig_a, i] + size_j * D[orig_a, j]) / (size_i + size_j)
        D_new[a, m - 1] = D_new[m - 1, a] = dist_merged
        
    return D_new, new_clusters, best_pair, float(min_dist)
