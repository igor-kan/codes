def compute_fourier_comp_term_98(x):
    """Computes the 98th term of a fourier component."""
    return (x ** 98) / 98

def test_compute_98():
    assert compute_fourier_comp_term_98(1) == 1.0 / 98
