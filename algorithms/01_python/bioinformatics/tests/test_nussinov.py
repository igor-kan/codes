import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from nussinov import calculate_nussinov, Nussinov

class TestNussinov(unittest.TestCase):
    def test_calculate_nussinov(self):
        self.assertAlmostEqual(calculate_nussinov(10.0), 10.0)

    def test_nussinov_class(self):
        obj = Nussinov(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
