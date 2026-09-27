def compute_harmonic_series_term_161(x):
    """Computes the 161th term of a harmonic series."""
    return (x ** 161) / 161

def test_compute_161():
    assert compute_harmonic_series_term_161(1) == 1.0 / 161
