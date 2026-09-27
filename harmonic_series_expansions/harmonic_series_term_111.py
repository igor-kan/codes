def compute_harmonic_series_term_111(x):
    """Computes the 111th term of a harmonic series."""
    return (x ** 111) / 111

def test_compute_111():
    assert compute_harmonic_series_term_111(1) == 1.0 / 111
