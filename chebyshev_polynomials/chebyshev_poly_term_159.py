def compute_chebyshev_poly_term_159(x):
    """Computes the 159th term of a chebyshev polynomial."""
    return (x ** 159) / 159

def test_compute_159():
    assert compute_chebyshev_poly_term_159(1) == 1.0 / 159
