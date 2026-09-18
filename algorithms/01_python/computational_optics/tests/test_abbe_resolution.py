import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from abbe_resolution import calculate_abbe_resolution, AbbeResolution

class TestAbbeResolution(unittest.TestCase):
    def test_calculate_abbe_resolution(self):
        self.assertAlmostEqual(calculate_abbe_resolution(10.0), 10.0)

    def test_abbe_resolution_class(self):
        obj = AbbeResolution(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
