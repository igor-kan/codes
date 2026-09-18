import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from harmonic_oscillator import calculate_harmonic_oscillator, HarmonicOscillator

class TestHarmonicOscillator(unittest.TestCase):
    def test_calculate_harmonic_oscillator(self):
        self.assertAlmostEqual(calculate_harmonic_oscillator(10.0), 10.0)

    def test_harmonic_oscillator_class(self):
        obj = HarmonicOscillator(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
