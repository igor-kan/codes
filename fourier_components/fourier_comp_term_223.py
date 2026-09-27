def compute_fourier_comp_term_223(x):
    """Computes the 223th term of a fourier component."""
    return (x ** 223) / 223

def test_compute_223():
    assert compute_fourier_comp_term_223(1) == 1.0 / 223
