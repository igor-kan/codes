from semiclassical_tunneling_wkb import gamow_tunneling_factor


def test_gamow():
    T = gamow_tunneling_factor(1.0, 5.0, 0.5)
    assert 0.0 < T < 1.0
