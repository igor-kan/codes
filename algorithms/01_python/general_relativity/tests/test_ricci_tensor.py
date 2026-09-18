import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ricci_tensor import calculate_ricci_tensor, RicciTensor

class TestRicciTensor(unittest.TestCase):
    def test_calculate_ricci_tensor(self):
        self.assertAlmostEqual(calculate_ricci_tensor(10.0), 10.0)

    def test_ricci_tensor_class(self):
        obj = RicciTensor(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
