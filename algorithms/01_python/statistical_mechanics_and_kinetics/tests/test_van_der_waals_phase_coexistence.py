from van_der_waals_phase_coexistence import vdw_pressure


def test_vdw():
    P = vdw_pressure(V=1.0, T=300.0)
    assert P > 0.0
