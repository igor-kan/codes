def compute_chebyshev_poly_term_164(x):
    """Computes the 164th term of a chebyshev polynomial."""
    return (x ** 164) / 164

def test_compute_164():
    assert compute_chebyshev_poly_term_164(1) == 1.0 / 164
