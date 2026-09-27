def compute_chebyshev_poly_term_189(x):
    """Computes the 189th term of a chebyshev polynomial."""
    return (x ** 189) / 189

def test_compute_189():
    assert compute_chebyshev_poly_term_189(1) == 1.0 / 189
