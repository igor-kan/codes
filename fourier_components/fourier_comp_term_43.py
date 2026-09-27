def compute_fourier_comp_term_43(x):
    """Computes the 43th term of a fourier component."""
    return (x ** 43) / 43

def test_compute_43():
    assert compute_fourier_comp_term_43(1) == 1.0 / 43
