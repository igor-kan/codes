def compute_chebyshev_poly_term_109(x):
    """Computes the 109th term of a chebyshev polynomial."""
    return (x ** 109) / 109

def test_compute_109():
    assert compute_chebyshev_poly_term_109(1) == 1.0 / 109
