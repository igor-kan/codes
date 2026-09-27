def compute_fourier_comp_term_13(x):
    """Computes the 13th term of a fourier component."""
    return (x ** 13) / 13

def test_compute_13():
    assert compute_fourier_comp_term_13(1) == 1.0 / 13
