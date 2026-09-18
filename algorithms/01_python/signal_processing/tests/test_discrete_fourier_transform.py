import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from discrete_fourier_transform import calculate_discrete_fourier_transform, DiscreteFourierTransform

class TestDiscreteFourierTransform(unittest.TestCase):
    def test_calculate_discrete_fourier_transform(self):
        self.assertAlmostEqual(calculate_discrete_fourier_transform(10.0), 10.0)

    def test_discrete_fourier_transform_class(self):
        obj = DiscreteFourierTransform(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
