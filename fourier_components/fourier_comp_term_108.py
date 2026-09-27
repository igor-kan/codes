def compute_fourier_comp_term_108(x):
    """Computes the 108th term of a fourier component."""
    return (x ** 108) / 108

def test_compute_108():
    assert compute_fourier_comp_term_108(1) == 1.0 / 108
