import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fiber_optics import calculate_fiber_optics, FiberOptics

class TestFiberOptics(unittest.TestCase):
    def test_calculate_fiber_optics(self):
        self.assertAlmostEqual(calculate_fiber_optics(10.0), 10.0)

    def test_fiber_optics_class(self):
        obj = FiberOptics(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
