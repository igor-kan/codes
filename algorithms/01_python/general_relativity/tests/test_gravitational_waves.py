import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gravitational_waves import calculate_gravitational_waves, GravitationalWaves

class TestGravitationalWaves(unittest.TestCase):
    def test_calculate_gravitational_waves(self):
        self.assertAlmostEqual(calculate_gravitational_waves(10.0), 10.0)

    def test_gravitational_waves_class(self):
        obj = GravitationalWaves(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
