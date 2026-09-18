import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stokes_parameters import calculate_stokes_parameters, StokesParameters

class TestStokesParameters(unittest.TestCase):
    def test_calculate_stokes_parameters(self):
        self.assertAlmostEqual(calculate_stokes_parameters(10.0), 10.0)

    def test_stokes_parameters_class(self):
        obj = StokesParameters(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
