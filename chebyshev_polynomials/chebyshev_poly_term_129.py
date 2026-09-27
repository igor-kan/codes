def compute_chebyshev_poly_term_129(x):
    """Computes the 129th term of a chebyshev polynomial."""
    return (x ** 129) / 129

def test_compute_129():
    assert compute_chebyshev_poly_term_129(1) == 1.0 / 129
