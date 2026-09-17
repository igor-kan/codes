"""Unit tests for Euler Equations of Rigid Body."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from euler_equations_rigid_body import EulerRigidBody


class TestEulerRigidBody(unittest.TestCase):
    def test_intermediate_axis_unstable(self):
        # Moments I_1 = 1.0, I_2 = 2.0, I_3 = 3.0
        top = EulerRigidBody([1.0, 2.0, 3.0])
        l1, l2 = top.intermediate_axis_instability_eigenvalues(w0=5.0)
        # For intermediate axis, eigenvalues are purely real => exponential instability!
        self.assertGreater(np.real(l1), 0.0)
        self.assertEqual(np.imag(l1), 0.0)


if __name__ == "__main__":
    unittest.main()
