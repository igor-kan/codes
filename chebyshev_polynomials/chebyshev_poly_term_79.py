def compute_chebyshev_poly_term_79(x):
    """Computes the 79th term of a chebyshev polynomial."""
    return (x ** 79) / 79

def test_compute_79():
    assert compute_chebyshev_poly_term_79(1) == 1.0 / 79
