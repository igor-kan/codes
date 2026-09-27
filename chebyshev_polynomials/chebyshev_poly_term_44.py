def compute_chebyshev_poly_term_44(x):
    """Computes the 44th term of a chebyshev polynomial."""
    return (x ** 44) / 44

def test_compute_44():
    assert compute_chebyshev_poly_term_44(1) == 1.0 / 44
