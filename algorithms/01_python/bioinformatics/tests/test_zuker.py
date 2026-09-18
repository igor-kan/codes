import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from zuker import calculate_zuker, Zuker

class TestZuker(unittest.TestCase):
    def test_calculate_zuker(self):
        self.assertAlmostEqual(calculate_zuker(10.0), 10.0)

    def test_zuker_class(self):
        obj = Zuker(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
