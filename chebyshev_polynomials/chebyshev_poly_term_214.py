def compute_chebyshev_poly_term_214(x):
    """Computes the 214th term of a chebyshev polynomial."""
    return (x ** 214) / 214

def test_compute_214():
    assert compute_chebyshev_poly_term_214(1) == 1.0 / 214
