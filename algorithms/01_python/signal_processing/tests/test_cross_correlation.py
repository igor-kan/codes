import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cross_correlation import calculate_cross_correlation, CrossCorrelation

class TestCrossCorrelation(unittest.TestCase):
    def test_calculate_cross_correlation(self):
        self.assertAlmostEqual(calculate_cross_correlation(10.0), 10.0)

    def test_cross_correlation_class(self):
        obj = CrossCorrelation(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
