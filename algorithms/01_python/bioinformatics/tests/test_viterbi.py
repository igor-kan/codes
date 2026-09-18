import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from viterbi import calculate_viterbi, Viterbi

class TestViterbi(unittest.TestCase):
    def test_calculate_viterbi(self):
        self.assertAlmostEqual(calculate_viterbi(10.0), 10.0)

    def test_viterbi_class(self):
        obj = Viterbi(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
