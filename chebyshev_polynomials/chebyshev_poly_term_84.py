def compute_chebyshev_poly_term_84(x):
    """Computes the 84th term of a chebyshev polynomial."""
    return (x ** 84) / 84

def test_compute_84():
    assert compute_chebyshev_poly_term_84(1) == 1.0 / 84
