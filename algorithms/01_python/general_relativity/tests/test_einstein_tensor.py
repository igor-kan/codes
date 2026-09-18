import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from einstein_tensor import calculate_einstein_tensor, EinsteinTensor

class TestEinsteinTensor(unittest.TestCase):
    def test_calculate_einstein_tensor(self):
        self.assertAlmostEqual(calculate_einstein_tensor(10.0), 10.0)

    def test_einstein_tensor_class(self):
        obj = EinsteinTensor(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
