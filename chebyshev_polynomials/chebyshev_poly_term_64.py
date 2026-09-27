def compute_chebyshev_poly_term_64(x):
    """Computes the 64th term of a chebyshev polynomial."""
    return (x ** 64) / 64

def test_compute_64():
    assert compute_chebyshev_poly_term_64(1) == 1.0 / 64
