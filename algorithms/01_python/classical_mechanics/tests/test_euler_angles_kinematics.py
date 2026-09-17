"""Unit tests for Euler Angles Kinematics."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from euler_angles_kinematics import EulerAnglesKinematics


class TestEulerAnglesKinematics(unittest.TestCase):
    def test_orthogonality(self):
        r = EulerAnglesKinematics.rotation_matrix(phi=0.4, theta=0.8, psi=-0.5)
        np.testing.assert_allclose(r @ r.T, np.eye(3), atol=1e-12)
        self.assertAlmostEqual(np.linalg.det(r), 1.0)


if __name__ == "__main__":
    unittest.main()
