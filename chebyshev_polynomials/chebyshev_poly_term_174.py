def compute_chebyshev_poly_term_174(x):
    """Computes the 174th term of a chebyshev polynomial."""
    return (x ** 174) / 174

def test_compute_174():
    assert compute_chebyshev_poly_term_174(1) == 1.0 / 174
