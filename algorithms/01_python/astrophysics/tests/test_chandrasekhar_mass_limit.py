"""Unit tests for Chandrasekhar Mass Limit."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from chandrasekhar_mass_limit import ChandrasekharLimit


class TestChandrasekhar(unittest.TestCase):
    def test_solar_mass_range(self):
        m_solar = ChandrasekharLimit.in_solar_masses(mu_e=2.0)
        # Standard Chandrasekhar limit is ~1.4 to 1.46 solar masses
        self.assertTrue(1.40 <= m_solar <= 1.48)


if __name__ == "__main__":
    unittest.main()
