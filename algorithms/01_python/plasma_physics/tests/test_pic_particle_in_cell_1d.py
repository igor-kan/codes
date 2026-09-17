"""Unit tests for Particle-in-Cell 1D."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pic_particle_in_cell_1d import ParticleInCell1D


class TestPIC(unittest.TestCase):
    def test_charge_conservation(self):
        pic = ParticleInCell1D(num_grid_nodes=20, box_length=10.0, num_particles=100)
        rho = pic.deposit_charge_cic()
        # Sum of deposited charge must equal total number of particles
        self.assertAlmostEqual(np.sum(rho), 100.0)


if __name__ == "__main__":
    unittest.main()
