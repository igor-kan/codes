def compute_fourier_comp_term_3(x):
    """Computes the 3th term of a fourier component."""
    return (x ** 3) / 3

def test_compute_3():
    assert compute_fourier_comp_term_3(1) == 1.0 / 3
