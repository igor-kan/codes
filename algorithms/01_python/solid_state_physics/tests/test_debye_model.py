import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from debye_model import calculate_debye_model, DebyeModel

class TestDebyeModel(unittest.TestCase):
    def test_calculate_debye_model(self):
        self.assertAlmostEqual(calculate_debye_model(10.0), 10.0)

    def test_debye_model_class(self):
        obj = DebyeModel(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
