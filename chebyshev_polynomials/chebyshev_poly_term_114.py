def compute_chebyshev_poly_term_114(x):
    """Computes the 114th term of a chebyshev polynomial."""
    return (x ** 114) / 114

def test_compute_114():
    assert compute_chebyshev_poly_term_114(1) == 1.0 / 114
