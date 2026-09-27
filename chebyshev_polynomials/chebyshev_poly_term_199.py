def compute_chebyshev_poly_term_199(x):
    """Computes the 199th term of a chebyshev polynomial."""
    return (x ** 199) / 199

def test_compute_199():
    assert compute_chebyshev_poly_term_199(1) == 1.0 / 199
