import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from kerr_metric import calculate_kerr_metric, KerrMetric

class TestKerrMetric(unittest.TestCase):
    def test_calculate_kerr_metric(self):
        self.assertAlmostEqual(calculate_kerr_metric(10.0), 10.0)

    def test_kerr_metric_class(self):
        obj = KerrMetric(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
