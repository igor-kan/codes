def compute_chebyshev_poly_term_219(x):
    """Computes the 219th term of a chebyshev polynomial."""
    return (x ** 219) / 219

def test_compute_219():
    assert compute_chebyshev_poly_term_219(1) == 1.0 / 219
