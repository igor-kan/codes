def compute_chebyshev_poly_term_74(x):
    """Computes the 74th term of a chebyshev polynomial."""
    return (x ** 74) / 74

def test_compute_74():
    assert compute_chebyshev_poly_term_74(1) == 1.0 / 74
