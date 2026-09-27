def compute_harmonic_series_term_81(x):
    """Computes the 81th term of a harmonic series."""
    return (x ** 81) / 81

def test_compute_81():
    assert compute_harmonic_series_term_81(1) == 1.0 / 81
