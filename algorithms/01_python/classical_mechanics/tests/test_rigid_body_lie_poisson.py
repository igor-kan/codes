"""Unit tests for Lie-Poisson Rigid Body."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rigid_body_lie_poisson import LiePoissonRigidBody


class TestLiePoissonRigidBody(unittest.TestCase):
    def test_casimir_and_energy_conservation(self):
        lp = LiePoissonRigidBody(principal_moments=[1.0, 2.0, 3.0])
        m0 = [1.0, 1.0, 1.0]
        dm = lp.time_derivative(m0)
        # dot{C} = m . dot{m} = m . (m x omega) == 0
        self.assertAlmostEqual(np.dot(m0, dm), 0.0)
        # dot{H} = grad H . dot{m} = omega . (m x omega) == 0
        omega = np.array(m0) / [1.0, 2.0, 3.0]
        self.assertAlmostEqual(np.dot(omega, dm), 0.0)


if __name__ == "__main__":
    unittest.main()
