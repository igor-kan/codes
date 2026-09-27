def compute_fourier_comp_term_73(x):
    """Computes the 73th term of a fourier component."""
    return (x ** 73) / 73

def test_compute_73():
    assert compute_fourier_comp_term_73(1) == 1.0 / 73
