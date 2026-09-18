import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from kd_tree import calculate_kd_tree, KdTree

class TestKdTree(unittest.TestCase):
    def test_calculate_kd_tree(self):
        self.assertAlmostEqual(calculate_kd_tree(10.0), 10.0)

    def test_kd_tree_class(self):
        obj = KdTree(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
