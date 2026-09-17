"""Unit tests for Stress-Energy Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from stress_energy_tensor import StressEnergyTensor


class TestStressEnergyTensor(unittest.TestCase):
    def test_radiation_fluid_traceless(self):
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        rho = 300.0
        p = rho / 3.0
        u = [1.0, 0.0, 0.0, 0.0]
        t = StressEnergyTensor.perfect_fluid(rho, p, u, eta)
        trace_val = t.trace(eta)
        self.assertAlmostEqual(trace_val, 0.0)


if __name__ == "__main__":
    unittest.main()
