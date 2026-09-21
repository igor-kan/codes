import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from riemann_liouville_fractional import fractional_integral_rl

def test_fractional_integral_constant():
    # I^1 of constant 1.0 is t
    t = np.linspace(0.0, 1.0, 100)
    f = np.ones_like(t)
    res = fractional_integral_rl(f, t, alpha=1.0)
    assert np.allclose(res[10:], t[10:], rtol=1e-1)
