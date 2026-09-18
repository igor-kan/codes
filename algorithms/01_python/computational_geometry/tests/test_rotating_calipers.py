import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rotating_calipers import calculate_rotating_calipers, RotatingCalipers

class TestRotatingCalipers(unittest.TestCase):
    def test_calculate_rotating_calipers(self):
        self.assertAlmostEqual(calculate_rotating_calipers(10.0), 10.0)

    def test_rotating_calipers_class(self):
        obj = RotatingCalipers(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
