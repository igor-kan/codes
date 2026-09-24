from quantum_tunneling_barrier import barrier_transmission_coefficient


def test_tunneling():
    V0 = 5.0
    a = 1.0
    T_sub = barrier_transmission_coefficient(2.5, V0, a)
    assert 0.0 < T_sub < 1.0
    T_super = barrier_transmission_coefficient(10.0, V0, a)
    assert T_super > T_sub
