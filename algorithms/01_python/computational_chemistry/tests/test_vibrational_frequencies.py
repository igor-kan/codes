import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vibrational_frequencies import calculate_vibrational_frequencies, VibrationalFrequencies

class TestVibrationalFrequencies(unittest.TestCase):
    def test_calculate_vibrational_frequencies(self):
        self.assertAlmostEqual(calculate_vibrational_frequencies(10.0), 10.0)

    def test_vibrational_frequencies_class(self):
        obj = VibrationalFrequencies(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
