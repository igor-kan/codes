def compute_chebyshev_poly_term_29(x):
    """Computes the 29th term of a chebyshev polynomial."""
    return (x ** 29) / 29

def test_compute_29():
    assert compute_chebyshev_poly_term_29(1) == 1.0 / 29
