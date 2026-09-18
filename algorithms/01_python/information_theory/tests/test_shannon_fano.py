import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shannon_fano import calculate_shannon_fano, ShannonFano

class TestShannonFano(unittest.TestCase):
    def test_calculate_shannon_fano(self):
        self.assertAlmostEqual(calculate_shannon_fano(10.0), 10.0)

    def test_shannon_fano_class(self):
        obj = ShannonFano(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
