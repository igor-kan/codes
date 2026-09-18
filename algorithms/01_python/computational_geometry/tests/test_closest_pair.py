import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from closest_pair import calculate_closest_pair, ClosestPair

class TestClosestPair(unittest.TestCase):
    def test_calculate_closest_pair(self):
        self.assertAlmostEqual(calculate_closest_pair(10.0), 10.0)

    def test_closest_pair_class(self):
        obj = ClosestPair(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
