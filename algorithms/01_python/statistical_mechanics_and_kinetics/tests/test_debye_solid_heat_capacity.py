import numpy as np
from debye_solid_heat_capacity import debye_heat_capacity


def test_debye():
    c = debye_heat_capacity(T=10.0, T_D=300.0)
    assert c > 0.0
