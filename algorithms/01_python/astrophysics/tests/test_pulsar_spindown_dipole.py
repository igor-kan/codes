"""Unit tests for pulsar spindown."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pulsar_spindown_dipole import PulsarSpindown


class TestPulsar(unittest.TestCase):
    def test_crab_pulsar(self):
        # Crab pulsar: P ~ 0.033 s, P_dot ~ 4.2e-13 s/s
        age_seconds = PulsarSpindown.characteristic_age(0.033, 4.2e-13)
        age_years = age_seconds / (365.25 * 86400)
        # Characteristic age ~ 1240 years
        self.assertTrue(1000 <= age_years <= 1500)


if __name__ == "__main__":
    unittest.main()
