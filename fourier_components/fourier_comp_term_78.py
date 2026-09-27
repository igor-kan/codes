def compute_fourier_comp_term_78(x):
    """Computes the 78th term of a fourier component."""
    return (x ** 78) / 78

def test_compute_78():
    assert compute_fourier_comp_term_78(1) == 1.0 / 78
