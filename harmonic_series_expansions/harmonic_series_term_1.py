def compute_harmonic_series_term_1(x):
    """Computes the 1th term of a harmonic series."""
    return (x ** 1) / 1

def test_compute_1():
    assert compute_harmonic_series_term_1(1) == 1.0 / 1
