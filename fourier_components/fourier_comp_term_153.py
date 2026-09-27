def compute_fourier_comp_term_153(x):
    """Computes the 153th term of a fourier component."""
    return (x ** 153) / 153

def test_compute_153():
    assert compute_fourier_comp_term_153(1) == 1.0 / 153
