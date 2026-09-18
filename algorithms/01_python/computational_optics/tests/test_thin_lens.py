import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from thin_lens import calculate_thin_lens, ThinLens

class TestThinLens(unittest.TestCase):
    def test_calculate_thin_lens(self):
        self.assertAlmostEqual(calculate_thin_lens(10.0), 10.0)

    def test_thin_lens_class(self):
        obj = ThinLens(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
