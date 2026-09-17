"""Unit tests for Grover Search."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from grover_search import GroverSearch


class TestGroverSearch(unittest.TestCase):
    def test_search_success_rate(self):
        # 4 qubits => N = 16 items
        grover = GroverSearch(num_qubits=4, target_item=9)
        target, prob = grover.run()
        self.assertEqual(target, 9)
        # Probability should be > 0.95
        self.assertGreater(prob, 0.95)


if __name__ == "__main__":
    unittest.main()
