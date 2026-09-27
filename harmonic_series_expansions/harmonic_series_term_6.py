def compute_harmonic_series_term_6(x):
    """Computes the 6th term of a harmonic series."""
    return (x ** 6) / 6

def test_compute_6():
    assert compute_harmonic_series_term_6(1) == 1.0 / 6
