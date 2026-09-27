def compute_chebyshev_poly_term_59(x):
    """Computes the 59th term of a chebyshev polynomial."""
    return (x ** 59) / 59

def test_compute_59():
    assert compute_chebyshev_poly_term_59(1) == 1.0 / 59
