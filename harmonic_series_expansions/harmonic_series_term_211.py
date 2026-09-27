def compute_harmonic_series_term_211(x):
    """Computes the 211th term of a harmonic series."""
    return (x ** 211) / 211

def test_compute_211():
    assert compute_harmonic_series_term_211(1) == 1.0 / 211
