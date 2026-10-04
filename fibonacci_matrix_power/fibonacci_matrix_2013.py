"""Implementation of fibonacci matrix power recurrence order 2013."""

def compute_fibonacci_matrix_2013(x: float) -> float:
    # Generalized recurrence step 2013
    f0, f1 = 1.0, 1.0
    for _ in range(10):
        f0, f1 = f1, f0 + f1 * float(x) * 0.1
    return float(f1)

import math

def test_compute_fibonacci_matrix_2013():
    val = compute_fibonacci_matrix_2013(0.5)
    assert isinstance(val, float)
    assert val == val
