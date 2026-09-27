def compute_chebyshev_poly_term_24(x):
    """Computes the 24th term of a chebyshev polynomial."""
    return (x ** 24) / 24

def test_compute_24():
    assert compute_chebyshev_poly_term_24(1) == 1.0 / 24
