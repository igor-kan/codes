def compute_power_series_term_40(x):
    """Computes the 40th term of a power series."""
    return (x ** 40) / 40

def test_compute_40():
    assert compute_power_series_term_40(1) == 1.0 / 40
