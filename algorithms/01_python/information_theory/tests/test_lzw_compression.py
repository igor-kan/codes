import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lzw_compression import calculate_lzw_compression, LzwCompression

class TestLzwCompression(unittest.TestCase):
    def test_calculate_lzw_compression(self):
        self.assertAlmostEqual(calculate_lzw_compression(10.0), 10.0)

    def test_lzw_compression_class(self):
        obj = LzwCompression(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
