import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from schwarzschild_metric import calculate_schwarzschild_metric, SchwarzschildMetric

class TestSchwarzschildMetric(unittest.TestCase):
    def test_calculate_schwarzschild_metric(self):
        self.assertAlmostEqual(calculate_schwarzschild_metric(10.0), 10.0)

    def test_schwarzschild_metric_class(self):
        obj = SchwarzschildMetric(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
