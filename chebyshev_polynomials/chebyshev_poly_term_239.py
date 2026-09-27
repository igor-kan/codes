def compute_chebyshev_poly_term_239(x):
    """Computes the 239th term of a chebyshev polynomial."""
    return (x ** 239) / 239

def test_compute_239():
    assert compute_chebyshev_poly_term_239(1) == 1.0 / 239
