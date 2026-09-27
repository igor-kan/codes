def compute_chebyshev_poly_term_139(x):
    """Computes the 139th term of a chebyshev polynomial."""
    return (x ** 139) / 139

def test_compute_139():
    assert compute_chebyshev_poly_term_139(1) == 1.0 / 139
