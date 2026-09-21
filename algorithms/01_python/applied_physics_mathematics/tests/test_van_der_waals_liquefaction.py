import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from van_der_waals_liquefaction import vdw_pressure, critical_constants

def test_vdw():
    Tc, Pc, vc = critical_constants()
    assert Tc > 0 and Pc > 0 and vc > 0
    p = vdw_pressure(np.array([vc]), Tc)
    assert np.isclose(p[0], Pc, rtol=1e-2)
