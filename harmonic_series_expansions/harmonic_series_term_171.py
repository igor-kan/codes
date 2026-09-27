def compute_harmonic_series_term_171(x):
    """Computes the 171th term of a harmonic series."""
    return (x ** 171) / 171

def test_compute_171():
    assert compute_harmonic_series_term_171(1) == 1.0 / 171
