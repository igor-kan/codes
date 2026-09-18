import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fabry_perot import calculate_fabry_perot, FabryPerot

class TestFabryPerot(unittest.TestCase):
    def test_calculate_fabry_perot(self):
        self.assertAlmostEqual(calculate_fabry_perot(10.0), 10.0)

    def test_fabry_perot_class(self):
        obj = FabryPerot(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
