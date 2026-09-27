def compute_chebyshev_poly_term_94(x):
    """Computes the 94th term of a chebyshev polynomial."""
    return (x ** 94) / 94

def test_compute_94():
    assert compute_chebyshev_poly_term_94(1) == 1.0 / 94
