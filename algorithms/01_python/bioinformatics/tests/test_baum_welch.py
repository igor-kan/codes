import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from baum_welch import calculate_baum_welch, BaumWelch

class TestBaumWelch(unittest.TestCase):
    def test_calculate_baum_welch(self):
        self.assertAlmostEqual(calculate_baum_welch(10.0), 10.0)

    def test_baum_welch_class(self):
        obj = BaumWelch(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
