import numpy as np
from fresnel_diffraction_integral import fresnel_propagate_1d


def test_fresnel_energy_conservation():
    # Gaussian beam propagates with conserved L2 norm (Parseval's theorem)
    n = 256
    dx = 1e-5
    x = (np.arange(n) - n / 2) * dx
    w0 = 5e-4
    u0 = np.exp(- (x / w0)**2).astype(complex)

    energy_0 = np.sum(np.abs(u0)**2)
    u_z = fresnel_propagate_1d(u0, dx, wavelength=632.8e-9, z=0.05)
    energy_z = np.sum(np.abs(u_z)**2)

    assert np.isclose(energy_0, energy_z, rtol=1e-10)
