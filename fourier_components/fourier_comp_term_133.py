def compute_fourier_comp_term_133(x):
    """Computes the 133th term of a fourier component."""
    return (x ** 133) / 133

def test_compute_133():
    assert compute_fourier_comp_term_133(1) == 1.0 / 133
