import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chan_algorithm import calculate_chan_algorithm, ChanAlgorithm

class TestChanAlgorithm(unittest.TestCase):
    def test_calculate_chan_algorithm(self):
        self.assertAlmostEqual(calculate_chan_algorithm(10.0), 10.0)

    def test_chan_algorithm_class(self):
        obj = ChanAlgorithm(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
