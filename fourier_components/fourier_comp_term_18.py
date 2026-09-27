def compute_fourier_comp_term_18(x):
    """Computes the 18th term of a fourier component."""
    return (x ** 18) / 18

def test_compute_18():
    assert compute_fourier_comp_term_18(1) == 1.0 / 18
