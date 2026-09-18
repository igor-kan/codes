import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bwt_rle import calculate_bwt_rle, BwtRle

class TestBwtRle(unittest.TestCase):
    def test_calculate_bwt_rle(self):
        self.assertAlmostEqual(calculate_bwt_rle(10.0), 10.0)

    def test_bwt_rle_class(self):
        obj = BwtRle(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
