import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from upgma import calculate_upgma, Upgma

class TestUpgma(unittest.TestCase):
    def test_calculate_upgma(self):
        self.assertAlmostEqual(calculate_upgma(10.0), 10.0)

    def test_upgma_class(self):
        obj = Upgma(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
