import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mutual_information import calculate_mutual_information, MutualInformation

class TestMutualInformation(unittest.TestCase):
    def test_calculate_mutual_information(self):
        self.assertAlmostEqual(calculate_mutual_information(10.0), 10.0)

    def test_mutual_information_class(self):
        obj = MutualInformation(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
