def compute_chebyshev_poly_term_54(x):
    """Computes the 54th term of a chebyshev polynomial."""
    return (x ** 54) / 54

def test_compute_54():
    assert compute_chebyshev_poly_term_54(1) == 1.0 / 54
