import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ising_model import calculate_ising_model, IsingModel

class TestIsingModel(unittest.TestCase):
    def test_calculate_ising_model(self):
        self.assertAlmostEqual(calculate_ising_model(10.0), 10.0)

    def test_ising_model_class(self):
        obj = IsingModel(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
