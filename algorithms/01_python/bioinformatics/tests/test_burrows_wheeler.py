import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from burrows_wheeler import calculate_burrows_wheeler, BurrowsWheeler

class TestBurrowsWheeler(unittest.TestCase):
    def test_calculate_burrows_wheeler(self):
        self.assertAlmostEqual(calculate_burrows_wheeler(10.0), 10.0)

    def test_burrows_wheeler_class(self):
        obj = BurrowsWheeler(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
