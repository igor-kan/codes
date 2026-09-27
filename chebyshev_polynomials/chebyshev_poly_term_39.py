def compute_chebyshev_poly_term_39(x):
    """Computes the 39th term of a chebyshev polynomial."""
    return (x ** 39) / 39

def test_compute_39():
    assert compute_chebyshev_poly_term_39(1) == 1.0 / 39
