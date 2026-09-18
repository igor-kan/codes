import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from interference import calculate_interference, Interference

class TestInterference(unittest.TestCase):
    def test_calculate_interference(self):
        self.assertAlmostEqual(calculate_interference(10.0), 10.0)

    def test_interference_class(self):
        obj = Interference(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
