def compute_harmonic_series_term_51(x):
    """Computes the 51th term of a harmonic series."""
    return (x ** 51) / 51

def test_compute_51():
    assert compute_harmonic_series_term_51(1) == 1.0 / 51
