import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from inverse_fft import calculate_inverse_fft, InverseFft

class TestInverseFft(unittest.TestCase):
    def test_calculate_inverse_fft(self):
        self.assertAlmostEqual(calculate_inverse_fft(10.0), 10.0)

    def test_inverse_fft_class(self):
        obj = InverseFft(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
