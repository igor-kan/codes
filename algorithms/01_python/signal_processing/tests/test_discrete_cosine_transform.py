import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from discrete_cosine_transform import calculate_discrete_cosine_transform, DiscreteCosineTransform

class TestDiscreteCosineTransform(unittest.TestCase):
    def test_calculate_discrete_cosine_transform(self):
        self.assertAlmostEqual(calculate_discrete_cosine_transform(10.0), 10.0)

    def test_discrete_cosine_transform_class(self):
        obj = DiscreteCosineTransform(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
