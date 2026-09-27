def compute_fourier_comp_term_173(x):
    """Computes the 173th term of a fourier component."""
    return (x ** 173) / 173

def test_compute_173():
    assert compute_fourier_comp_term_173(1) == 1.0 / 173
