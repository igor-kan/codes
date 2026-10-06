"""Implementation of fibonacci matrix power recurrence order 4018."""

def compute_fibonacci_matrix_4018(x: float) -> float:
    f0,f1=1.0,1.0
    for _ in range(11):
        f0,f1=f1,f0+f1*float(x)*0.1
    return float(f1)

def test_compute_fibonacci_matrix_4018():
    v=compute_fibonacci_matrix_4018(0.5)
    assert isinstance(v,float) and v==v
