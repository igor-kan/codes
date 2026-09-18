import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from kullback_leibler import calculate_kullback_leibler, KullbackLeibler

class TestKullbackLeibler(unittest.TestCase):
    def test_calculate_kullback_leibler(self):
        self.assertAlmostEqual(calculate_kullback_leibler(10.0), 10.0)

    def test_kullback_leibler_class(self):
        obj = KullbackLeibler(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
