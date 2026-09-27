def compute_geometric_series_term_2(x):
    """Computes the 2th term of a geometric series."""
    return (x ** 2) / 2

def test_compute_2():
    assert compute_geometric_series_term_2(1) == 1.0 / 2
