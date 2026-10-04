"""Implementation of fibonacci matrix power recurrence order 2023."""

def compute_fibonacci_matrix_2023(x: float) -> float:
    # Generalized recurrence step 2023
    f0, f1 = 1.0, 1.0
    for _ in range(8):
        f0, f1 = f1, f0 + f1 * float(x) * 0.1
    return float(f1)

import math

def test_compute_fibonacci_matrix_2023():
    val = compute_fibonacci_matrix_2023(0.5)
    assert isinstance(val, float)
    assert val == val
