def compute_fourier_comp_term_88(x):
    """Computes the 88th term of a fourier component."""
    return (x ** 88) / 88

def test_compute_88():
    assert compute_fourier_comp_term_88(1) == 1.0 / 88
