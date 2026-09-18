import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from snells_law import calculate_snells_law, SnellsLaw

class TestSnellsLaw(unittest.TestCase):
    def test_calculate_snells_law(self):
        self.assertAlmostEqual(calculate_snells_law(10.0), 10.0)

    def test_snells_law_class(self):
        obj = SnellsLaw(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
