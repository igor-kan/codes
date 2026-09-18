import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from curie_weiss import calculate_curie_weiss, CurieWeiss

class TestCurieWeiss(unittest.TestCase):
    def test_calculate_curie_weiss(self):
        self.assertAlmostEqual(calculate_curie_weiss(10.0), 10.0)

    def test_curie_weiss_class(self):
        obj = CurieWeiss(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
