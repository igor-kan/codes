import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from needleman_wunsch import calculate_needleman_wunsch, NeedlemanWunsch

class TestNeedlemanWunsch(unittest.TestCase):
    def test_calculate_needleman_wunsch(self):
        self.assertAlmostEqual(calculate_needleman_wunsch(10.0), 10.0)

    def test_needleman_wunsch_class(self):
        obj = NeedlemanWunsch(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
