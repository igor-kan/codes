def compute_fourier_comp_term_123(x):
    """Computes the 123th term of a fourier component."""
    return (x ** 123) / 123

def test_compute_123():
    assert compute_fourier_comp_term_123(1) == 1.0 / 123
