def compute_chebyshev_poly_term_179(x):
    """Computes the 179th term of a chebyshev polynomial."""
    return (x ** 179) / 179

def test_compute_179():
    assert compute_chebyshev_poly_term_179(1) == 1.0 / 179
