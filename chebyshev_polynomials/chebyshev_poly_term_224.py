def compute_chebyshev_poly_term_224(x):
    """Computes the 224th term of a chebyshev polynomial."""
    return (x ** 224) / 224

def test_compute_224():
    assert compute_chebyshev_poly_term_224(1) == 1.0 / 224
