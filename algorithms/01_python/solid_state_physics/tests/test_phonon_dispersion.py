import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from phonon_dispersion import calculate_phonon_dispersion, PhononDispersion

class TestPhononDispersion(unittest.TestCase):
    def test_calculate_phonon_dispersion(self):
        self.assertAlmostEqual(calculate_phonon_dispersion(10.0), 10.0)

    def test_phonon_dispersion_class(self):
        obj = PhononDispersion(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
