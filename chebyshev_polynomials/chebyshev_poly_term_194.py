def compute_chebyshev_poly_term_194(x):
    """Computes the 194th term of a chebyshev polynomial."""
    return (x ** 194) / 194

def test_compute_194():
    assert compute_chebyshev_poly_term_194(1) == 1.0 / 194
