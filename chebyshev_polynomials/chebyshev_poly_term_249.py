def compute_chebyshev_poly_term_249(x):
    """Computes the 249th term of a chebyshev polynomial."""
    return (x ** 249) / 249

def test_compute_249():
    assert compute_chebyshev_poly_term_249(1) == 1.0 / 249
