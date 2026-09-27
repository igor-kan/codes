def compute_fourier_comp_term_193(x):
    """Computes the 193th term of a fourier component."""
    return (x ** 193) / 193

def test_compute_193():
    assert compute_fourier_comp_term_193(1) == 1.0 / 193
