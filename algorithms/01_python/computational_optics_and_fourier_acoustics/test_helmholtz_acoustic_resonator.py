import numpy as np
from helmholtz_acoustic_resonator import helmholtz_resonance_frequency


def test_helmholtz_bottle():
    # 1 liter bottle (V = 1e-3 m^3), neck diameter 2 cm, neck length 5 cm
    f0 = helmholtz_resonance_frequency(volume_V=1e-3, neck_diameter=0.02, neck_length=0.05)
    # Typical beer bottle resonance is ~100-200 Hz
    assert 100.0 < f0 < 200.0
