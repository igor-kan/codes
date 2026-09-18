import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from christoffel_symbols import calculate_christoffel_symbols, ChristoffelSymbols

class TestChristoffelSymbols(unittest.TestCase):
    def test_calculate_christoffel_symbols(self):
        self.assertAlmostEqual(calculate_christoffel_symbols(10.0), 10.0)

    def test_christoffel_symbols_class(self):
        obj = ChristoffelSymbols(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
