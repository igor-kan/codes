import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dipole_moment import calculate_dipole_moment, DipoleMoment

class TestDipoleMoment(unittest.TestCase):
    def test_calculate_dipole_moment(self):
        self.assertAlmostEqual(calculate_dipole_moment(10.0), 10.0)

    def test_dipole_moment_class(self):
        obj = DipoleMoment(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
