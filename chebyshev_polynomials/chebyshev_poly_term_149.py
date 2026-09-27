def compute_chebyshev_poly_term_149(x):
    """Computes the 149th term of a chebyshev polynomial."""
    return (x ** 149) / 149

def test_compute_149():
    assert compute_chebyshev_poly_term_149(1) == 1.0 / 149
