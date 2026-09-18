import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fast_fourier_transform import calculate_fast_fourier_transform, FastFourierTransform

class TestFastFourierTransform(unittest.TestCase):
    def test_calculate_fast_fourier_transform(self):
        self.assertAlmostEqual(calculate_fast_fourier_transform(10.0), 10.0)

    def test_fast_fourier_transform_class(self):
        obj = FastFourierTransform(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
