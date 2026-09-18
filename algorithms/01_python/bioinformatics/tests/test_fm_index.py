import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fm_index import calculate_fm_index, FmIndex

class TestFmIndex(unittest.TestCase):
    def test_calculate_fm_index(self):
        self.assertAlmostEqual(calculate_fm_index(10.0), 10.0)

    def test_fm_index_class(self):
        obj = FmIndex(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
