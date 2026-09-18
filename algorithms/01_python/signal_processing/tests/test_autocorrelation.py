import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from autocorrelation import calculate_autocorrelation, Autocorrelation

class TestAutocorrelation(unittest.TestCase):
    def test_calculate_autocorrelation(self):
        self.assertAlmostEqual(calculate_autocorrelation(10.0), 10.0)

    def test_autocorrelation_class(self):
        obj = Autocorrelation(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
