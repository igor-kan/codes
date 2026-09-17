"""Unit tests for seismic reflection NMO."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from seismic_reflection_nmo import SeismicReflectionNMO


class TestNMO(unittest.TestCase):
    def test_zero_offset(self):
        t = SeismicReflectionNMO.travel_time(offset_x=0.0, zero_offset_time_t0=1.5, v_rms=2500.0)
        self.assertEqual(t, 1.5)
        dnmo = SeismicReflectionNMO.normal_moveout(offset_x=0.0, zero_offset_time_t0=1.5, v_rms=2500.0)
        self.assertEqual(dnmo, 0.0)


if __name__ == "__main__":
    unittest.main()
