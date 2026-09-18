import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hartree_fock import calculate_hartree_fock, HartreeFock

class TestHartreeFock(unittest.TestCase):
    def test_calculate_hartree_fock(self):
        self.assertAlmostEqual(calculate_hartree_fock(10.0), 10.0)

    def test_hartree_fock_class(self):
        obj = HartreeFock(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
