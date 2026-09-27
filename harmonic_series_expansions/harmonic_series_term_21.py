def compute_harmonic_series_term_21(x):
    """Computes the 21th term of a harmonic series."""
    return (x ** 21) / 21

def test_compute_21():
    assert compute_harmonic_series_term_21(1) == 1.0 / 21
