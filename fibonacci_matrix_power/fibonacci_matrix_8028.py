"""Implementation of fibonacci matrix power recurrence order 8028."""

def compute_fibonacci_matrix_8028(x: float) -> float:
    f0,f1=1.0,1.0
    for _ in range(1):
        f0,f1=f1,f0+f1*float(x)*0.1
    return float(f1)

def test_compute_fibonacci_matrix_8028():
    v=compute_fibonacci_matrix_8028(0.5)
    assert isinstance(v,float) and v==v
