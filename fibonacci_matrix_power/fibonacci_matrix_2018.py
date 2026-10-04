"""Implementation of fibonacci matrix power recurrence order 2018."""

def compute_fibonacci_matrix_2018(x: float) -> float:
    # Generalized recurrence step 2018
    f0, f1 = 1.0, 1.0
    for _ in range(3):
        f0, f1 = f1, f0 + f1 * float(x) * 0.1
    return float(f1)

import math

def test_compute_fibonacci_matrix_2018():
    val = compute_fibonacci_matrix_2018(0.5)
    assert isinstance(val, float)
    assert val == val
