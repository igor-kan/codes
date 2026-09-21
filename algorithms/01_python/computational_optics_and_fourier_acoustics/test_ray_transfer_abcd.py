import numpy as np
from ray_transfer_abcd import free_space_matrix, thin_lens_matrix, gaussian_q_parameter, transform_gaussian_q, beam_radius_from_q


def test_gaussian_propagation():
    wl = 1064e-9
    w0 = 1e-3  # 1 mm waist
    q0 = gaussian_q_parameter(w0, wl, z=0.0)

    # Propagate 2 meters in free space
    d = 2.0
    M = free_space_matrix(d)
    q_out = transform_gaussian_q(q0, M)

    w_out = beam_radius_from_q(q_out, wl)
    z_R = np.pi * (w0**2) / wl
    expected_w = w0 * np.sqrt(1.0 + (d / z_R)**2)
    assert np.isclose(w_out, expected_w)
