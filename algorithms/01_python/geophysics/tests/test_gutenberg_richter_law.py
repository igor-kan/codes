"""Unit tests for Gutenberg-Richter law."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gutenberg_richter_law import GutenbergRichterLaw


class TestGutenbergRichter(unittest.TestCase):
    def test_aki_utsu_estimator(self):
        # Generate synthetic exponential distribution: p(M) ~ exp(-beta * (M - M_min))
        # where beta = b * ln(10). For b=1.0, beta = ln(10) ~ 2.30258
        np.random.seed(42)
        m_min = 2.0
        beta = 1.0 * np.log(10.0)
        synth_m = m_min + np.random.exponential(scale=1.0 / beta, size=5000)
        b_est = GutenbergRichterLaw.estimate_b_value_aki_utsu(synth_m, m_cutoff=m_min, bin_width=0.0)
        self.assertAlmostEqual(b_est, 1.0, places=1)


if __name__ == "__main__":
    unittest.main()
