"""Unit tests for Quaternion Rigid Body Kinematics."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quaternion_rigid_body import QuaternionRigidBody


class TestQuaternionRigidBody(unittest.TestCase):
    def test_identity_quaternion(self):
        quat = QuaternionRigidBody([1.0, 0.0, 0.0, 0.0])
        r = quat.to_rotation_matrix()
        np.testing.assert_allclose(r, np.eye(3))

    def test_derivative_preserves_norm(self):
        quat = QuaternionRigidBody([1.0, 0.0, 0.0, 0.0])
        q_dot = quat.kinematic_derivative([0.0, 0.0, 2.0])
        # d/dt (q . q) = 2 q . q_dot = 0
        self.assertAlmostEqual(np.dot(quat.q, q_dot), 0.0)


if __name__ == "__main__":
    unittest.main()
