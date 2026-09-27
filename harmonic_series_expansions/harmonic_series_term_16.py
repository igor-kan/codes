def compute_harmonic_series_term_16(x):
    """Computes the 16th term of a harmonic series."""
    return (x ** 16) / 16

def test_compute_16():
    assert compute_harmonic_series_term_16(1) == 1.0 / 16
