import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bloch_theorem import calculate_bloch_theorem, BlochTheorem

class TestBlochTheorem(unittest.TestCase):
    def test_calculate_bloch_theorem(self):
        self.assertAlmostEqual(calculate_bloch_theorem(10.0), 10.0)

    def test_bloch_theorem_class(self):
        obj = BlochTheorem(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
