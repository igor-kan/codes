import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hall_effect import calculate_hall_effect, HallEffect

class TestHallEffect(unittest.TestCase):
    def test_calculate_hall_effect(self):
        self.assertAlmostEqual(calculate_hall_effect(10.0), 10.0)

    def test_hall_effect_class(self):
        obj = HallEffect(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
