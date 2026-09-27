def compute_chebyshev_poly_term_154(x):
    """Computes the 154th term of a chebyshev polynomial."""
    return (x ** 154) / 154

def test_compute_154():
    assert compute_chebyshev_poly_term_154(1) == 1.0 / 154
