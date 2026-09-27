def compute_harmonic_series_term_201(x):
    """Computes the 201th term of a harmonic series."""
    return (x ** 201) / 201

def test_compute_201():
    assert compute_harmonic_series_term_201(1) == 1.0 / 201
