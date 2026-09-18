import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ricci_scalar import calculate_ricci_scalar, RicciScalar

class TestRicciScalar(unittest.TestCase):
    def test_calculate_ricci_scalar(self):
        self.assertAlmostEqual(calculate_ricci_scalar(10.0), 10.0)

    def test_ricci_scalar_class(self):
        obj = RicciScalar(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
