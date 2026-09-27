def compute_geometric_series_term_52(x):
    """Computes the 52th term of a geometric series."""
    return (x ** 52) / 52

def test_compute_52():
    assert compute_geometric_series_term_52(1) == 1.0 / 52
