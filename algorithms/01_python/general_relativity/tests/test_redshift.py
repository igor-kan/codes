import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from redshift import calculate_redshift, Redshift

class TestRedshift(unittest.TestCase):
    def test_calculate_redshift(self):
        self.assertAlmostEqual(calculate_redshift(10.0), 10.0)

    def test_redshift_class(self):
        obj = Redshift(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
