def compute_fourier_comp_term_213(x):
    """Computes the 213th term of a fourier component."""
    return (x ** 213) / 213

def test_compute_213():
    assert compute_fourier_comp_term_213(1) == 1.0 / 213
