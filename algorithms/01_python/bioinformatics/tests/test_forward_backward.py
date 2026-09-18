import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from forward_backward import calculate_forward_backward, ForwardBackward

class TestForwardBackward(unittest.TestCase):
    def test_calculate_forward_backward(self):
        self.assertAlmostEqual(calculate_forward_backward(10.0), 10.0)

    def test_forward_backward_class(self):
        obj = ForwardBackward(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
