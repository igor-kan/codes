def compute_fourier_comp_term_8(x):
    """Computes the 8th term of a fourier component."""
    return (x ** 8) / 8

def test_compute_8():
    assert compute_fourier_comp_term_8(1) == 1.0 / 8
