import numpy as np
from jones_calculus_polarization import linear_polarizer, quarter_wave_plate, half_wave_plate


def test_crossed_polarizers():
    pol_h = linear_polarizer(0.0)
    pol_v = linear_polarizer(np.pi / 2.0)
    # Crossed polarizers extinguish completely
    combined = pol_v @ pol_h
    assert np.allclose(combined, np.zeros((2, 2)), atol=1e-12)


def test_circular_polarization_generation():
    # Linear polarization at 45 deg through fast-axis=0 QWP generates circular polarization
    qwp = quarter_wave_plate(0.0)
    j_in = np.array([1.0, 1.0]) / np.sqrt(2.0)
    j_out = qwp @ j_in
    # |Ex| = |Ey| and phase difference is pi/2
    assert np.isclose(abs(j_out[0]), abs(j_out[1]))
    assert np.isclose(np.angle(j_out[1]) - np.angle(j_out[0]), -np.pi / 2.0)
