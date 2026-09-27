def compute_harmonic_series_term_121(x):
    """Computes the 121th term of a harmonic series."""
    return (x ** 121) / 121

def test_compute_121():
    assert compute_harmonic_series_term_121(1) == 1.0 / 121
