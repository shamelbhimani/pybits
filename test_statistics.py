import unittest

import statistics
from statistics import Statistics


class TestStatistics(unittest.TestCase):

    def test_sample_mean(self):
        a = Statistics([1, 2, 3])
        self.assertEqual(a.sample_mean(), 2)
