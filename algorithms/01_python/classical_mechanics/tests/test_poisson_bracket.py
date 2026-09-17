"""Unit tests for Poisson Bracket."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poisson_bracket import PoissonBracket


class TestPoissonBracket(unittest.TestCase):
    def test_fundamental_brackets(self):
        # {q_i, p_j} = delta_{ij}, {q_i, q_j} = 0, {p_i, p_j} = 0
        pb = PoissonBracket(degrees_of_freedom=1)
        q_func = lambda z: z[0]
        p_func = lambda z: z[1]

        z0 = [2.0, 3.0]
        self.assertAlmostEqual(pb.bracket(q_func, p_func, z0), 1.0, places=4)
        self.assertAlmostEqual(pb.bracket(p_func, q_func, z0), -1.0, places=4)
        self.assertAlmostEqual(pb.bracket(q_func, q_func, z0), 0.0, places=4)

    def test_jacobi_identity(self):
        pb = PoissonBracket(degrees_of_freedom=1)
        f = lambda z: z[0]**2
        g = lambda z: z[1]**2
        h = lambda z: z[0] * z[1]
        z0 = [1.5, 2.5]
        self.assertTrue(pb.verify_jacobi_identity(f, g, h, z0))


if __name__ == "__main__":
    unittest.main()
