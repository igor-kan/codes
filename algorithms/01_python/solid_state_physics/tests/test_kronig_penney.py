import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from kronig_penney import calculate_kronig_penney, KronigPenney

class TestKronigPenney(unittest.TestCase):
    def test_calculate_kronig_penney(self):
        self.assertAlmostEqual(calculate_kronig_penney(10.0), 10.0)

    def test_kronig_penney_class(self):
        obj = KronigPenney(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
