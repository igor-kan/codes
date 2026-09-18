import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from arithmetic_coding import calculate_arithmetic_coding, ArithmeticCoding

class TestArithmeticCoding(unittest.TestCase):
    def test_calculate_arithmetic_coding(self):
        self.assertAlmostEqual(calculate_arithmetic_coding(10.0), 10.0)

    def test_arithmetic_coding_class(self):
        obj = ArithmeticCoding(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
