def compute_fourier_comp_term_163(x):
    """Computes the 163th term of a fourier component."""
    return (x ** 163) / 163

def test_compute_163():
    assert compute_fourier_comp_term_163(1) == 1.0 / 163
