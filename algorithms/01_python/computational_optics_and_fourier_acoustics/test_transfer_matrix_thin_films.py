import numpy as np
from transfer_matrix_thin_films import multilayer_film_transmittance_reflectance


def test_quarter_wave_antireflection():
    # Quarter-wave anti-reflection coating on glass (n_glass = 1.5):
    # n_coating = sqrt(n_air * n_glass) = sqrt(1.5) approx 1.2247
    wl = 500e-9
    n_glass = 1.5
    n_ar = np.sqrt(n_glass)
    d_ar = wl / (4.0 * n_ar)

    R, T = multilayer_film_transmittance_reflectance(wl, [n_ar], [d_ar], n_glass, n_ambient=1.0)
    # Reflectance should be zero at design wavelength
    assert np.isclose(R, 0.0, atol=1e-5)
    assert np.isclose(T, 1.0, atol=1e-5)
