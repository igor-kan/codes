def compute_chebyshev_poly_term_124(x):
    """Computes the 124th term of a chebyshev polynomial."""
    return (x ** 124) / 124

def test_compute_124():
    assert compute_chebyshev_poly_term_124(1) == 1.0 / 124
