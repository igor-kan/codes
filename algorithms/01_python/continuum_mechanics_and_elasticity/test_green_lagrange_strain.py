import numpy as np
from green_lagrange_strain import deformation_gradient, green_lagrange_strain, infinitesimal_strain


def test_small_vs_large_strain():
    # For very small displacement gradient, E matches eps
    grad_small = np.array([[1e-5, 2e-5, 0], [2e-5, -1e-5, 0], [0, 0, 5e-6]])
    E = green_lagrange_strain(grad_small)
    eps = infinitesimal_strain(grad_small)
    assert np.allclose(E, eps, atol=1e-8)

    # For finite rigid rotation, E = 0 but eps != 0
    theta = np.radians(30.0)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    grad_rot = R - np.eye(3)
    E_rot = green_lagrange_strain(grad_rot)
    assert np.allclose(E_rot, np.zeros((3, 3)), atol=1e-12)
