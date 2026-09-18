import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from graham_scan import calculate_graham_scan, GrahamScan

class TestGrahamScan(unittest.TestCase):
    def test_calculate_graham_scan(self):
        self.assertAlmostEqual(calculate_graham_scan(10.0), 10.0)

    def test_graham_scan_class(self):
        obj = GrahamScan(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
