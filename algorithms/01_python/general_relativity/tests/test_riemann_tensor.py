import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from riemann_tensor import calculate_riemann_tensor, RiemannTensor

class TestRiemannTensor(unittest.TestCase):
    def test_calculate_riemann_tensor(self):
        self.assertAlmostEqual(calculate_riemann_tensor(10.0), 10.0)

    def test_riemann_tensor_class(self):
        obj = RiemannTensor(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
