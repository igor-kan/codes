def compute_fourier_comp_term_113(x):
    """Computes the 113th term of a fourier component."""
    return (x ** 113) / 113

def test_compute_113():
    assert compute_fourier_comp_term_113(1) == 1.0 / 113
