import numpy as np
from coherence_michelson_interferometer import gaussian_spectral_visibility, fringe_visibility_from_intensity


def test_visibility():
    assert fringe_visibility_from_intensity(10.0, 0.0) == 1.0
    assert fringe_visibility_from_intensity(5.0, 5.0) == 0.0

    # Visibility decays as path difference increases
    v0 = gaussian_spectral_visibility(0.0, 1e-3)
    v1 = gaussian_spectral_visibility(1e-3, 1e-3)
    assert np.isclose(v0, 1.0)
    assert v1 < v0
