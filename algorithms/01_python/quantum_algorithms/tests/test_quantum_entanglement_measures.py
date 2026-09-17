"""Unit tests for Entanglement Measures."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_entanglement_measures import EntanglementMeasures


class TestEntanglementMeasures(unittest.TestCase):
    def test_bell_state_negativity(self):
        # Bell state has negativity 0.5 and log negativity 1.0
        psi = np.array([1.0, 0.0, 0.0, 1.0]) / np.sqrt(2.0)
        rho_bell = np.outer(psi, psi)
        neg = EntanglementMeasures.negativity(rho_bell)
        log_neg = EntanglementMeasures.logarithmic_negativity(rho_bell)
        self.assertAlmostEqual(neg, 0.5)
        self.assertAlmostEqual(log_neg, 1.0)


if __name__ == "__main__":
    unittest.main()
