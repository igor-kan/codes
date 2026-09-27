def compute_harmonic_series_term_11(x):
    """Computes the 11th term of a harmonic series."""
    return (x ** 11) / 11

def test_compute_11():
    assert compute_harmonic_series_term_11(1) == 1.0 / 11
