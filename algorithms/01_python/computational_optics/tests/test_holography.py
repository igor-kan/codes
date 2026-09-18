import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from holography import calculate_holography, Holography

class TestHolography(unittest.TestCase):
    def test_calculate_holography(self):
        self.assertAlmostEqual(calculate_holography(10.0), 10.0)

    def test_holography_class(self):
        obj = Holography(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
