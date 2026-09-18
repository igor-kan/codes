import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hamming_code import calculate_hamming_code, HammingCode

class TestHammingCode(unittest.TestCase):
    def test_calculate_hamming_code(self):
        self.assertAlmostEqual(calculate_hamming_code(10.0), 10.0)

    def test_hamming_code_class(self):
        obj = HammingCode(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
