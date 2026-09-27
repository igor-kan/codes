def compute_harmonic_series_term_231(x):
    """Computes the 231th term of a harmonic series."""
    return (x ** 231) / 231

def test_compute_231():
    assert compute_harmonic_series_term_231(1) == 1.0 / 231
