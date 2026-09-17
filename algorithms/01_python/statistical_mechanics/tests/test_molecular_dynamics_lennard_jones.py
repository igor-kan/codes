"""Unit tests for Lennard-Jones MD."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from molecular_dynamics_lennard_jones import LennardJonesMD


class TestLennardJonesMD(unittest.TestCase):
    def test_energy_conservation(self):
        pos = np.array([[1.0, 1.0, 1.0], [2.2, 1.0, 1.0]])
        vel = np.array([[0.1, 0.0, 0.0], [-0.1, 0.0, 0.0]])
        md = LennardJonesMD(pos, vel, box_length=10.0)
        e0 = md.verlet_step(dt=0.001)
        e1 = md.verlet_step(dt=0.001)
        self.assertAlmostEqual(e0, e1, places=3)


if __name__ == "__main__":
    unittest.main()
