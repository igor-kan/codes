def compute_fourier_comp_term_23(x):
    """Computes the 23th term of a fourier component."""
    return (x ** 23) / 23

def test_compute_23():
    assert compute_fourier_comp_term_23(1) == 1.0 / 23
