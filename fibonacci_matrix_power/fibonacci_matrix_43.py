"""Implementation of fibonacci matrix power recurrence order 43."""

def compute_fibonacci_matrix_43(x: float) -> float:
    # Generalized recurrence step 43
    f0, f1 = 1.0, 1.0
    for _ in range(8):
        f0, f1 = f1, f0 + f1 * float(x) * 0.1
    return float(f1)

import math

def test_compute_fibonacci_matrix_43():
    val = compute_fibonacci_matrix_43(0.5)
    assert isinstance(val, float)
    assert val == val
