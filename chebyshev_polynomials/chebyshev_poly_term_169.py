def compute_chebyshev_poly_term_169(x):
    """Computes the 169th term of a chebyshev polynomial."""
    return (x ** 169) / 169

def test_compute_169():
    assert compute_chebyshev_poly_term_169(1) == 1.0 / 169
