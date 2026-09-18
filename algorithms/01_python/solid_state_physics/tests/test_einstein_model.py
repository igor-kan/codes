import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from einstein_model import calculate_einstein_model, EinsteinModel

class TestEinsteinModel(unittest.TestCase):
    def test_calculate_einstein_model(self):
        self.assertAlmostEqual(calculate_einstein_model(10.0), 10.0)

    def test_einstein_model_class(self):
        obj = EinsteinModel(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
