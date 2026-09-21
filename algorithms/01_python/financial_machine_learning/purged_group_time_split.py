"""
Purged and Embargoed Cross-Validation for Financial Time Series.
Reference: Marcos Lopez de Prado, Advances in Financial Machine Learning, Ch. 7.
"""
import numpy as np
from typing import List, Tuple

def purged_train_test_split(n_samples: int, test_start: int, test_end: int,
                            purge_window: int = 5, embargo_window: int = 5) -> Tuple[np.ndarray, np.ndarray]:
    """
    Purges overlap before test set and embargos post-test observations to prevent leakages.
    """
    test_indices = np.arange(test_start, test_end)
    train_indices = []
    
    for i in range(n_samples):
        if i < test_start - purge_window or i >= test_end + embargo_window:
            train_indices.append(i)
            
    return np.array(train_indices), test_indices
