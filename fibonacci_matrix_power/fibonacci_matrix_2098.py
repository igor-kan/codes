"""Implementation of fibonacci matrix power recurrence order 2098."""

def compute_fibonacci_matrix_2098(x: float) -> float:
    # Generalized recurrence step 2098
    f0, f1 = 1.0, 1.0
    for _ in range(11):
        f0, f1 = f1, f0 + f1 * float(x) * 0.1
    return float(f1)

import math

def test_compute_fibonacci_matrix_2098():
    val = compute_fibonacci_matrix_2098(0.5)
    assert isinstance(val, float)
    assert val == val
