import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lennard_jones import calculate_lennard_jones, LennardJones

class TestLennardJones(unittest.TestCase):
    def test_calculate_lennard_jones(self):
        self.assertAlmostEqual(calculate_lennard_jones(10.0), 10.0)

    def test_lennard_jones_class(self):
        obj = LennardJones(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
