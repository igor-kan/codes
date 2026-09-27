def compute_fourier_comp_term_183(x):
    """Computes the 183th term of a fourier component."""
    return (x ** 183) / 183

def test_compute_183():
    assert compute_fourier_comp_term_183(1) == 1.0 / 183
