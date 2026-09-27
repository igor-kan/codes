def compute_fourier_comp_term_28(x):
    """Computes the 28th term of a fourier component."""
    return (x ** 28) / 28

def test_compute_28():
    assert compute_fourier_comp_term_28(1) == 1.0 / 28
