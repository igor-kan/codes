def compute_chebyshev_poly_term_4(x):
    """Computes the 4th term of a chebyshev polynomial."""
    return (x ** 4) / 4

def test_compute_4():
    assert compute_chebyshev_poly_term_4(1) == 1.0 / 4
