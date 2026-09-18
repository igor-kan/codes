import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from neighbor_joining import calculate_neighbor_joining, NeighborJoining

class TestNeighborJoining(unittest.TestCase):
    def test_calculate_neighbor_joining(self):
        self.assertAlmostEqual(calculate_neighbor_joining(10.0), 10.0)

    def test_neighbor_joining_class(self):
        obj = NeighborJoining(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
