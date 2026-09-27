def compute_fourier_comp_term_83(x):
    """Computes the 83th term of a fourier component."""
    return (x ** 83) / 83

def test_compute_83():
    assert compute_fourier_comp_term_83(1) == 1.0 / 83
