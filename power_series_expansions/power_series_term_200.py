def compute_power_series_term_200(x):
    """Computes the 200th term of a power series."""
    return (x ** 200) / 200

def test_compute_200():
    assert compute_power_series_term_200(1) == 1.0 / 200
