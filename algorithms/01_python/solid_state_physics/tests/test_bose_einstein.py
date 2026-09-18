import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bose_einstein import calculate_bose_einstein, BoseEinstein

class TestBoseEinstein(unittest.TestCase):
    def test_calculate_bose_einstein(self):
        self.assertAlmostEqual(calculate_bose_einstein(10.0), 10.0)

    def test_bose_einstein_class(self):
        obj = BoseEinstein(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
