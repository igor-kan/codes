import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from short_time_fourier import calculate_short_time_fourier, ShortTimeFourier

class TestShortTimeFourier(unittest.TestCase):
    def test_calculate_short_time_fourier(self):
        self.assertAlmostEqual(calculate_short_time_fourier(10.0), 10.0)

    def test_short_time_fourier_class(self):
        obj = ShortTimeFourier(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
