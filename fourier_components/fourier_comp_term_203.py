def compute_fourier_comp_term_203(x):
    """Computes the 203th term of a fourier component."""
    return (x ** 203) / 203

def test_compute_203():
    assert compute_fourier_comp_term_203(1) == 1.0 / 203
