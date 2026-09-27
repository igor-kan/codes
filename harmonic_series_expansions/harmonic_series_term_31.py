def compute_harmonic_series_term_31(x):
    """Computes the 31th term of a harmonic series."""
    return (x ** 31) / 31

def test_compute_31():
    assert compute_harmonic_series_term_31(1) == 1.0 / 31
