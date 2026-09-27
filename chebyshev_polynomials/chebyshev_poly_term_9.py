def compute_chebyshev_poly_term_9(x):
    """Computes the 9th term of a chebyshev polynomial."""
    return (x ** 9) / 9

def test_compute_9():
    assert compute_chebyshev_poly_term_9(1) == 1.0 / 9
