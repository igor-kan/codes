import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from blast_heuristic import calculate_blast_heuristic, BlastHeuristic

class TestBlastHeuristic(unittest.TestCase):
    def test_calculate_blast_heuristic(self):
        self.assertAlmostEqual(calculate_blast_heuristic(10.0), 10.0)

    def test_blast_heuristic_class(self):
        obj = BlastHeuristic(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
