"""Unit tests for Complex Potential Flow."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from potential_flow_complex import ComplexPotentialFlow


class TestComplexPotential(unittest.TestCase):
    def test_kutta_joukowski(self):
        lift = ComplexPotentialFlow.kutta_joukowski_lift(density=1.225, u_inf=50.0, circulation_gamma=10.0)
        self.assertAlmostEqual(lift, 612.5)


if __name__ == "__main__":
    unittest.main()
