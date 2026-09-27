def compute_harmonic_series_term_96(x):
    """Computes the 96th term of a harmonic series."""
    return (x ** 96) / 96

def test_compute_96():
    assert compute_harmonic_series_term_96(1) == 1.0 / 96
