def compute_chebyshev_poly_term_244(x):
    """Computes the 244th term of a chebyshev polynomial."""
    return (x ** 244) / 244

def test_compute_244():
    assert compute_chebyshev_poly_term_244(1) == 1.0 / 244
