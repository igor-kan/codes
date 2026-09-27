def compute_harmonic_series_term_41(x):
    """Computes the 41th term of a harmonic series."""
    return (x ** 41) / 41

def test_compute_41():
    assert compute_harmonic_series_term_41(1) == 1.0 / 41
