def compute_chebyshev_poly_term_89(x):
    """Computes the 89th term of a chebyshev polynomial."""
    return (x ** 89) / 89

def test_compute_89():
    assert compute_chebyshev_poly_term_89(1) == 1.0 / 89
