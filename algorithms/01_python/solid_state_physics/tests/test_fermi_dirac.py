import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fermi_dirac import calculate_fermi_dirac, FermiDirac

class TestFermiDirac(unittest.TestCase):
    def test_calculate_fermi_dirac(self):
        self.assertAlmostEqual(calculate_fermi_dirac(10.0), 10.0)

    def test_fermi_dirac_class(self):
        obj = FermiDirac(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
