"""Unit tests for Action-Angle Variables."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from action_angle_variables import ActionAngleTorus


class TestActionAngleVariables(unittest.TestCase):
    def test_torus_motion(self):
        aat = ActionAngleTorus(action_variables=[1.0, 2.0], fundamental_frequencies=[1.0, 2.0])
        angles = aat.angle_trajectory(t=np.pi, initial_angles=[0.0, 0.0])
        self.assertAlmostEqual(angles[0], np.pi)
        self.assertAlmostEqual(angles[1], 0.0, delta=1e-5)
        self.assertTrue(aat.is_resonant())


if __name__ == "__main__":
    unittest.main()
