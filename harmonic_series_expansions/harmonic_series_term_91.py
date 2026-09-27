def compute_harmonic_series_term_91(x):
    """Computes the 91th term of a harmonic series."""
    return (x ** 91) / 91

def test_compute_91():
    assert compute_harmonic_series_term_91(1) == 1.0 / 91
