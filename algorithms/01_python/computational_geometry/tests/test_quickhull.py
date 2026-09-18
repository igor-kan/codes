import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from quickhull import calculate_quickhull, Quickhull

class TestQuickhull(unittest.TestCase):
    def test_calculate_quickhull(self):
        self.assertAlmostEqual(calculate_quickhull(10.0), 10.0)

    def test_quickhull_class(self):
        obj = Quickhull(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
