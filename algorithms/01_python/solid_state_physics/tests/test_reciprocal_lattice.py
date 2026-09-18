import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reciprocal_lattice import calculate_reciprocal_lattice, ReciprocalLattice

class TestReciprocalLattice(unittest.TestCase):
    def test_calculate_reciprocal_lattice(self):
        self.assertAlmostEqual(calculate_reciprocal_lattice(10.0), 10.0)

    def test_reciprocal_lattice_class(self):
        obj = ReciprocalLattice(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
