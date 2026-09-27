def compute_chebyshev_poly_term_229(x):
    """Computes the 229th term of a chebyshev polynomial."""
    return (x ** 229) / 229

def test_compute_229():
    assert compute_chebyshev_poly_term_229(1) == 1.0 / 229
