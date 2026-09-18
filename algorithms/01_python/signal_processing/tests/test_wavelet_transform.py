import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from wavelet_transform import calculate_wavelet_transform, WaveletTransform

class TestWaveletTransform(unittest.TestCase):
    def test_calculate_wavelet_transform(self):
        self.assertAlmostEqual(calculate_wavelet_transform(10.0), 10.0)

    def test_wavelet_transform_class(self):
        obj = WaveletTransform(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
