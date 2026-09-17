"""Unit tests for seismic refraction."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from snells_law_seismic_refraction import SeismicRefraction


class TestRefraction(unittest.TestCase):
    def test_crossover(self):
        v1, v2, h = 2000.0, 4000.0, 100.0
        xc = SeismicRefraction.crossover_distance(h, v1, v2)
        # At crossover, direct wave time equals head wave time
        t_direct = xc / v1
        t_head = SeismicRefraction.head_wave_travel_time(xc, h, v1, v2)
        self.assertAlmostEqual(t_direct, t_head, places=4)


if __name__ == "__main__":
    unittest.main()
