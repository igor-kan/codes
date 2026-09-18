import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from diffraction_grating import calculate_diffraction_grating, DiffractionGrating

class TestDiffractionGrating(unittest.TestCase):
    def test_calculate_diffraction_grating(self):
        self.assertAlmostEqual(calculate_diffraction_grating(10.0), 10.0)

    def test_diffraction_grating_class(self):
        obj = DiffractionGrating(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
