import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fir_filter import calculate_fir_filter, FirFilter

class TestFirFilter(unittest.TestCase):
    def test_calculate_fir_filter(self):
        self.assertAlmostEqual(calculate_fir_filter(10.0), 10.0)

    def test_fir_filter_class(self):
        obj = FirFilter(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
