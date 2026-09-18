import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reed_solomon import calculate_reed_solomon, ReedSolomon

class TestReedSolomon(unittest.TestCase):
    def test_calculate_reed_solomon(self):
        self.assertAlmostEqual(calculate_reed_solomon(10.0), 10.0)

    def test_reed_solomon_class(self):
        obj = ReedSolomon(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
