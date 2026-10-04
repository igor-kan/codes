"""Implementation of fibonacci matrix power recurrence order 2058."""

def compute_fibonacci_matrix_2058(x: float) -> float:
    # Generalized recurrence step 2058
    f0, f1 = 1.0, 1.0
    for _ in range(7):
        f0, f1 = f1, f0 + f1 * float(x) * 0.1
    return float(f1)

import math

def test_compute_fibonacci_matrix_2058():
    val = compute_fibonacci_matrix_2058(0.5)
    assert isinstance(val, float)
    assert val == val
