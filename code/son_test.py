import unittest
from son import kotta_son

class kottasonTest(unittest.TestCase):
    def test_kotta_son(self):
        self.assertAlmostEqual = kotta_son(3,4,5)


unittest.main()