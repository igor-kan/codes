import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from jones_calculus import calculate_jones_calculus, JonesCalculus

class TestJonesCalculus(unittest.TestCase):
    def test_calculate_jones_calculus(self):
        self.assertAlmostEqual(calculate_jones_calculus(10.0), 10.0)

    def test_jones_calculus_class(self):
        obj = JonesCalculus(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
