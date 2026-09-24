from poincare_lindstedt_nonlinear_oscillator import poincare_lindstedt_duffing_freq


def test_duffing_freq():
    w0 = poincare_lindstedt_duffing_freq(A=1.0, eps=0.0)
    assert w0 == 1.0
    w_shifted = poincare_lindstedt_duffing_freq(A=2.0, eps=0.1)
    assert w_shifted == 1.15
