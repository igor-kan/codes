def compute_harmonic_series_term_221(x):
    """Computes the 221th term of a harmonic series."""
    return (x ** 221) / 221

def test_compute_221():
    assert compute_harmonic_series_term_221(1) == 1.0 / 221
