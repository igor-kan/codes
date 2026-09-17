"""Unit tests for Quantum Teleportation."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_teleportation import QuantumTeleportation


class TestQuantumTeleportation(unittest.TestCase):
    def test_state_fidelity(self):
        a_in = 0.6 + 0.0j
        b_in = 0.8j
        a_out, b_out = QuantumTeleportation.teleport(a_in, b_in)
        self.assertAlmostEqual(a_out, a_in)
        self.assertAlmostEqual(b_out, b_in)


if __name__ == "__main__":
    unittest.main()
