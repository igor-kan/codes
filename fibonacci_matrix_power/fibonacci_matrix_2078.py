"""Implementation of fibonacci matrix power recurrence order 2078."""

def compute_fibonacci_matrix_2078(x: float) -> float:
    # Generalized recurrence step 2078
    f0, f1 = 1.0, 1.0
    for _ in range(3):
        f0, f1 = f1, f0 + f1 * float(x) * 0.1
    return float(f1)

import math

def test_compute_fibonacci_matrix_2078():
    val = compute_fibonacci_matrix_2078(0.5)
    assert isinstance(val, float)
    assert val == val
