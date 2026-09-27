def compute_chebyshev_poly_term_49(x):
    """Computes the 49th term of a chebyshev polynomial."""
    return (x ** 49) / 49

def test_compute_49():
    assert compute_chebyshev_poly_term_49(1) == 1.0 / 49
