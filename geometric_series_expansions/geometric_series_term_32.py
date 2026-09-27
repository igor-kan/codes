def compute_geometric_series_term_32(x):
    """Computes the 32th term of a geometric series."""
    return (x ** 32) / 32

def test_compute_32():
    assert compute_geometric_series_term_32(1) == 1.0 / 32
