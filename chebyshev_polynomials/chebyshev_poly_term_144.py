def compute_chebyshev_poly_term_144(x):
    """Computes the 144th term of a chebyshev polynomial."""
    return (x ** 144) / 144

def test_compute_144():
    assert compute_chebyshev_poly_term_144(1) == 1.0 / 144
