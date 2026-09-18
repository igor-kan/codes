import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shannon_entropy import calculate_shannon_entropy, ShannonEntropy

class TestShannonEntropy(unittest.TestCase):
    def test_calculate_shannon_entropy(self):
        self.assertAlmostEqual(calculate_shannon_entropy(10.0), 10.0)

    def test_shannon_entropy_class(self):
        obj = ShannonEntropy(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
