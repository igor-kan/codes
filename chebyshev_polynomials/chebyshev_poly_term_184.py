def compute_chebyshev_poly_term_184(x):
    """Computes the 184th term of a chebyshev polynomial."""
    return (x ** 184) / 184

def test_compute_184():
    assert compute_chebyshev_poly_term_184(1) == 1.0 / 184
