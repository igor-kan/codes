import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hilbert_transform import calculate_hilbert_transform, HilbertTransform

class TestHilbertTransform(unittest.TestCase):
    def test_calculate_hilbert_transform(self):
        self.assertAlmostEqual(calculate_hilbert_transform(10.0), 10.0)

    def test_hilbert_transform_class(self):
        obj = HilbertTransform(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
