import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from smith_waterman import calculate_smith_waterman, SmithWaterman

class TestSmithWaterman(unittest.TestCase):
    def test_calculate_smith_waterman(self):
        self.assertAlmostEqual(calculate_smith_waterman(10.0), 10.0)

    def test_smith_waterman_class(self):
        obj = SmithWaterman(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
