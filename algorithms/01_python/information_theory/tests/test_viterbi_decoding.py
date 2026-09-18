import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from viterbi_decoding import calculate_viterbi_decoding, ViterbiDecoding

class TestViterbiDecoding(unittest.TestCase):
    def test_calculate_viterbi_decoding(self):
        self.assertAlmostEqual(calculate_viterbi_decoding(10.0), 10.0)

    def test_viterbi_decoding_class(self):
        obj = ViterbiDecoding(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
