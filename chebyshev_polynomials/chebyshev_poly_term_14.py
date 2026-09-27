def compute_chebyshev_poly_term_14(x):
    """Computes the 14th term of a chebyshev polynomial."""
    return (x ** 14) / 14

def test_compute_14():
    assert compute_chebyshev_poly_term_14(1) == 1.0 / 14
