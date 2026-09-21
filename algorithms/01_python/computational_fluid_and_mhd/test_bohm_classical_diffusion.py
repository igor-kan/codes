import numpy as np
from bohm_classical_diffusion import bohm_diffusion_coefficient, classical_perpendicular_diffusion


def test_diffusion_scaling():
    Te = 100.0  # 100 eV
    B1 = 1.0    # 1 Tesla
    B2 = 2.0    # 2 Tesla
    D_b1 = bohm_diffusion_coefficient(Te, B1)
    D_b2 = bohm_diffusion_coefficient(Te, B2)
    # Bohm scales as 1/B
    assert np.isclose(D_b1 / D_b2, 2.0)

    D_c1 = classical_perpendicular_diffusion(Te, B1, 1e5)
    D_c2 = classical_perpendicular_diffusion(Te, B2, 1e5)
    # Classical scales as 1/B^2
    assert np.isclose(D_c1 / D_c2, 4.0)
