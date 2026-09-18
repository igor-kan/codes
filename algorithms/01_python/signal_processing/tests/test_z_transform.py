import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from z_transform import calculate_z_transform, ZTransform

class TestZTransform(unittest.TestCase):
    def test_calculate_z_transform(self):
        self.assertAlmostEqual(calculate_z_transform(10.0), 10.0)

    def test_z_transform_class(self):
        obj = ZTransform(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
