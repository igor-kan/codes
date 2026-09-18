import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from channel_capacity import calculate_channel_capacity, ChannelCapacity

class TestChannelCapacity(unittest.TestCase):
    def test_calculate_channel_capacity(self):
        self.assertAlmostEqual(calculate_channel_capacity(10.0), 10.0)

    def test_channel_capacity_class(self):
        obj = ChannelCapacity(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
