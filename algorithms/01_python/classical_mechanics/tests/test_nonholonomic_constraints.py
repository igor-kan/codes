"""Unit tests for Non-Holonomic Constraints."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nonholonomic_constraints import NonHolonomicSystem


class TestNonHolonomicConstraints(unittest.TestCase):
    def test_knife_edge_sleigh_constraint(self):
        # 2D particle m=1 with velocity constraint v_y = 0 (knife edge along x)
        m = np.eye(2)
        system = NonHolonomicSystem(m)
        # Apply force in (x, y) = (10, 5)
        # Constraint A = [[0, 1]], drift = 0
        a = [[0.0, 1.0]]
        drift = [0.0]
        acc = system.constrained_acceleration(applied_forces=[10.0, 5.0], constraint_matrix=a, constraint_drift=drift)
        # x acceleration should be 10, y acceleration should be strictly 0
        self.assertAlmostEqual(acc[0], 10.0)
        self.assertAlmostEqual(acc[1], 0.0)


if __name__ == "__main__":
    unittest.main()
