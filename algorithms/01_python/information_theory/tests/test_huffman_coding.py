import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from huffman_coding import calculate_huffman_coding, HuffmanCoding

class TestHuffmanCoding(unittest.TestCase):
    def test_calculate_huffman_coding(self):
        self.assertAlmostEqual(calculate_huffman_coding(10.0), 10.0)

    def test_huffman_coding_class(self):
        obj = HuffmanCoding(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
