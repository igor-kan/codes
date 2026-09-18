import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from muller_calculus import calculate_muller_calculus, MullerCalculus

class TestMullerCalculus(unittest.TestCase):
    def test_calculate_muller_calculus(self):
        self.assertAlmostEqual(calculate_muller_calculus(10.0), 10.0)

    def test_muller_calculus_class(self):
        obj = MullerCalculus(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
