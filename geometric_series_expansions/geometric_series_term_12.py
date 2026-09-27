def compute_geometric_series_term_12(x):
    """Computes the 12th term of a geometric series."""
    return (x ** 12) / 12

def test_compute_12():
    assert compute_geometric_series_term_12(1) == 1.0 / 12
