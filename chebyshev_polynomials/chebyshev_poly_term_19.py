def compute_chebyshev_poly_term_19(x):
    """Computes the 19th term of a chebyshev polynomial."""
    return (x ** 19) / 19

def test_compute_19():
    assert compute_chebyshev_poly_term_19(1) == 1.0 / 19
