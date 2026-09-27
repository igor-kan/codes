def compute_harmonic_series_term_206(x):
    """Computes the 206th term of a harmonic series."""
    return (x ** 206) / 206

def test_compute_206():
    assert compute_harmonic_series_term_206(1) == 1.0 / 206
