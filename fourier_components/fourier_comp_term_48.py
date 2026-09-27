def compute_fourier_comp_term_48(x):
    """Computes the 48th term of a fourier component."""
    return (x ** 48) / 48

def test_compute_48():
    assert compute_fourier_comp_term_48(1) == 1.0 / 48
