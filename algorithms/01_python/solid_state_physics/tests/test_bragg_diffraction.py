import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bragg_diffraction import calculate_bragg_diffraction, BraggDiffraction

class TestBraggDiffraction(unittest.TestCase):
    def test_calculate_bragg_diffraction(self):
        self.assertAlmostEqual(calculate_bragg_diffraction(10.0), 10.0)

    def test_bragg_diffraction_class(self):
        obj = BraggDiffraction(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
