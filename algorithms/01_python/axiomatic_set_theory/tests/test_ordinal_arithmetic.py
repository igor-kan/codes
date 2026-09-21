import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ordinal_arithmetic import OrdinalTerm, ordinal_add

def test_ordinal_non_commutativity():
    # 1 + omega = omega
    one = [OrdinalTerm(0, 1)]
    omega = [OrdinalTerm(1, 1)]
    res = ordinal_add(one, omega)
    assert len(res) == 1 and res[0].exp == 1 and res[0].coeff == 1
    
    # omega + 1 != omega
    res2 = ordinal_add(omega, one)
    assert len(res2) == 2
