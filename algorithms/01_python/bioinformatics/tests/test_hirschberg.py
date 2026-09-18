import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hirschberg import calculate_hirschberg, Hirschberg

class TestHirschberg(unittest.TestCase):
    def test_calculate_hirschberg(self):
        self.assertAlmostEqual(calculate_hirschberg(10.0), 10.0)

    def test_hirschberg_class(self):
        obj = Hirschberg(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
