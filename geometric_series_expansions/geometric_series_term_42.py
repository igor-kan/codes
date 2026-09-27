def compute_geometric_series_term_42(x):
    """Computes the 42th term of a geometric series."""
    return (x ** 42) / 42

def test_compute_42():
    assert compute_geometric_series_term_42(1) == 1.0 / 42
