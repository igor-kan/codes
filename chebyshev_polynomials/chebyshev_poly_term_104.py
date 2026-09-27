def compute_chebyshev_poly_term_104(x):
    """Computes the 104th term of a chebyshev polynomial."""
    return (x ** 104) / 104

def test_compute_104():
    assert compute_chebyshev_poly_term_104(1) == 1.0 / 104
