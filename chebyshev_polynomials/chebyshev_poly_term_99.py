def compute_chebyshev_poly_term_99(x):
    """Computes the 99th term of a chebyshev polynomial."""
    return (x ** 99) / 99

def test_compute_99():
    assert compute_chebyshev_poly_term_99(1) == 1.0 / 99
