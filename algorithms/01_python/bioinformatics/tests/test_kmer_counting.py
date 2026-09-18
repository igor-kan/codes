import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from kmer_counting import calculate_kmer_counting, KmerCounting

class TestKmerCounting(unittest.TestCase):
    def test_calculate_kmer_counting(self):
        self.assertAlmostEqual(calculate_kmer_counting(10.0), 10.0)

    def test_kmer_counting_class(self):
        obj = KmerCounting(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
