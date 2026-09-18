import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from range_tree import calculate_range_tree, RangeTree

class TestRangeTree(unittest.TestCase):
    def test_calculate_range_tree(self):
        self.assertAlmostEqual(calculate_range_tree(10.0), 10.0)

    def test_range_tree_class(self):
        obj = RangeTree(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
