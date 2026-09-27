def compute_chebyshev_poly_term_34(x):
    """Computes the 34th term of a chebyshev polynomial."""
    return (x ** 34) / 34

def test_compute_34():
    assert compute_chebyshev_poly_term_34(1) == 1.0 / 34
