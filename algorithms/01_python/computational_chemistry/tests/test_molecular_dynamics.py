import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from molecular_dynamics import calculate_molecular_dynamics, MolecularDynamics

class TestMolecularDynamics(unittest.TestCase):
    def test_calculate_molecular_dynamics(self):
        self.assertAlmostEqual(calculate_molecular_dynamics(10.0), 10.0)

    def test_molecular_dynamics_class(self):
        obj = MolecularDynamics(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
