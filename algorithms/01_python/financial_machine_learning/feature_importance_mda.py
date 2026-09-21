"""
Mean Decrease Accuracy (MDA) Out-of-Sample Feature Importance.
Reference: Marcos Lopez de Prado, Advances in Financial Machine Learning, Ch. 8.
"""
import numpy as np
from typing import Callable

def permutation_mda(score_fn: Callable[[np.ndarray], float],
                    X: np.ndarray) -> np.ndarray:
    """Computes decrease in accuracy when each feature column is permuted."""
    baseline = score_fn(X)
    n_features = X.shape[1]
    importance = np.zeros(n_features)
    
    for j in range(n_features):
        X_perm = X.copy()
        np.random.shuffle(X_perm[:, j])
        score_perm = score_fn(X_perm)
        importance[j] = baseline - score_perm
        
    return importance
