def compute_fourier_comp_term_233(x):
    """Computes the 233th term of a fourier component."""
    return (x ** 233) / 233

def test_compute_233():
    assert compute_fourier_comp_term_233(1) == 1.0 / 233
