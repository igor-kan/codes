def compute_chebyshev_poly_term_204(x):
    """Computes the 204th term of a chebyshev polynomial."""
    return (x ** 204) / 204

def test_compute_204():
    assert compute_chebyshev_poly_term_204(1) == 1.0 / 204
