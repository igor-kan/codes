"""Unit tests for Takens delay embedding."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from takens_delay_embedding import TakensEmbedding


class TestTakens(unittest.TestCase):
    def test_embedding_dimensions(self):
        series = np.sin(np.linspace(0, 10, 100))
        m = 3
        tau = 2
        emb = TakensEmbedding.embed(series, dimension_m=m, delay_tau=tau)
        expected_rows = 100 - (3 - 1) * 2
        self.assertEqual(emb.shape, (expected_rows, 3))


if __name__ == "__main__":
    unittest.main()
