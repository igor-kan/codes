import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ray_tracing import calculate_ray_tracing, RayTracing

class TestRayTracing(unittest.TestCase):
    def test_calculate_ray_tracing(self):
        self.assertAlmostEqual(calculate_ray_tracing(10.0), 10.0)

    def test_ray_tracing_class(self):
        obj = RayTracing(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
