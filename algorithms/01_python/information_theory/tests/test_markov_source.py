import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from markov_source import calculate_markov_source, MarkovSource

class TestMarkovSource(unittest.TestCase):
    def test_calculate_markov_source(self):
        self.assertAlmostEqual(calculate_markov_source(10.0), 10.0)

    def test_markov_source_class(self):
        obj = MarkovSource(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
