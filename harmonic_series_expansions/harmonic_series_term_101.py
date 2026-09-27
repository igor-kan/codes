def compute_harmonic_series_term_101(x):
    """Computes the 101th term of a harmonic series."""
    return (x ** 101) / 101

def test_compute_101():
    assert compute_harmonic_series_term_101(1) == 1.0 / 101
