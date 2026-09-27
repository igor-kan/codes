def compute_harmonic_series_term_181(x):
    """Computes the 181th term of a harmonic series."""
    return (x ** 181) / 181

def test_compute_181():
    assert compute_harmonic_series_term_181(1) == 1.0 / 181
