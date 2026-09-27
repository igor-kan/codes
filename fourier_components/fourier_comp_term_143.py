def compute_fourier_comp_term_143(x):
    """Computes the 143th term of a fourier component."""
    return (x ** 143) / 143

def test_compute_143():
    assert compute_fourier_comp_term_143(1) == 1.0 / 143
