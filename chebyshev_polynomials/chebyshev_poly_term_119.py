def compute_chebyshev_poly_term_119(x):
    """Computes the 119th term of a chebyshev polynomial."""
    return (x ** 119) / 119

def test_compute_119():
    assert compute_chebyshev_poly_term_119(1) == 1.0 / 119
