import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from morse_potential import calculate_morse_potential, MorsePotential

class TestMorsePotential(unittest.TestCase):
    def test_calculate_morse_potential(self):
        self.assertAlmostEqual(calculate_morse_potential(10.0), 10.0)

    def test_morse_potential_class(self):
        obj = MorsePotential(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
