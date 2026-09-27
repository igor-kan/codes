def compute_fourier_comp_term_128(x):
    """Computes the 128th term of a fourier component."""
    return (x ** 128) / 128

def test_compute_128():
    assert compute_fourier_comp_term_128(1) == 1.0 / 128
