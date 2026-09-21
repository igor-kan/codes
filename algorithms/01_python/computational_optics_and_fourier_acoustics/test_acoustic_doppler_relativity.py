import numpy as np
from acoustic_doppler_relativity import acoustic_doppler_frequency, relativistic_optical_doppler


def test_doppler():
    f0 = 1000.0  # 1 kHz
    c = 340.0
    # Source approaching at 34 m/s (Mach 0.1)
    f_approach = acoustic_doppler_frequency(f0, c, v_receiver=0.0, v_source=34.0)
    assert f_approach > f0

    # Relativistic redshift for receding source
    f_red = relativistic_optical_doppler(f0, beta=0.5)
    assert f_red < f0
