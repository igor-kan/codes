from bloch_electron_periodic import is_allowed_band


def test_bands():
    assert is_allowed_band(1.0, P=0.0)
    assert not is_allowed_band(0.1, P=20.0)
