import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bond_angle import calculate_bond_angle, BondAngle

class TestBondAngle(unittest.TestCase):
    def test_calculate_bond_angle(self):
        self.assertAlmostEqual(calculate_bond_angle(10.0), 10.0)

    def test_bond_angle_class(self):
        obj = BondAngle(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
