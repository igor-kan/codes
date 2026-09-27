def compute_fourier_comp_term_103(x):
    """Computes the 103th term of a fourier component."""
    return (x ** 103) / 103

def test_compute_103():
    assert compute_fourier_comp_term_103(1) == 1.0 / 103
