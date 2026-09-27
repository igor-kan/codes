def compute_harmonic_series_term_61(x):
    """Computes the 61th term of a harmonic series."""
    return (x ** 61) / 61

def test_compute_61():
    assert compute_harmonic_series_term_61(1) == 1.0 / 61
