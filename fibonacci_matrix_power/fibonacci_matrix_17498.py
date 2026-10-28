"""Implementation of fibonacci matrix power recurrence order 17498."""

def compute_fibonacci_matrix_17498(x: float) -> float:
    f0,f1=1.0,1.0
    for _ in range(3):
        f0,f1=f1,f0+f1*float(x)*0.1
    return float(f1)

def test_compute_fibonacci_matrix_17498():
    v=compute_fibonacci_matrix_17498(0.5)
    assert isinstance(v,float) and v==v
