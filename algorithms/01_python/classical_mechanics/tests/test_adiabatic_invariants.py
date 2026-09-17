"""Unit tests for Adiabatic Invariants."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from adiabatic_invariants import AdiabaticInvariantOscillator


class TestAdiabaticInvariants(unittest.TestCase):
    def test_adiabatic_ratio(self):
        # Slowly varying frequency w(t) = 1.0 + 0.01 * t
        aio = AdiabaticInvariantOscillator(lambda t: 1.0 + 0.01 * t)
        # At turning point q = A, p = 0
        # E = 1/2 m w^2 A^2 => J = 1/2 m w A^2
        j1 = aio.action_variable(q=2.0, p=0.0, mass=1.0, t=0.0)
        # At t=0, w=1.0, E = 0.5 * 1.0 * 4.0 = 2.0 => J = 2.0
        self.assertAlmostEqual(j1, 2.0)


if __name__ == "__main__":
    unittest.main()
