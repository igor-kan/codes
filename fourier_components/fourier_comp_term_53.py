def compute_fourier_comp_term_53(x):
    """Computes the 53th term of a fourier component."""
    return (x ** 53) / 53

def test_compute_53():
    assert compute_fourier_comp_term_53(1) == 1.0 / 53
