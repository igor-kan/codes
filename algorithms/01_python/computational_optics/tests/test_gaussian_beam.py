import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gaussian_beam import calculate_gaussian_beam, GaussianBeam

class TestGaussianBeam(unittest.TestCase):
    def test_calculate_gaussian_beam(self):
        self.assertAlmostEqual(calculate_gaussian_beam(10.0), 10.0)

    def test_gaussian_beam_class(self):
        obj = GaussianBeam(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
