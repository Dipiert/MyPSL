import builtins
import sys
import unittest
from my_builtins import abs

class AbsTest(unittest.TestCase):

    def test_abs(self):
        # int
        self.assertEqual(abs(0), builtins.abs(0))
        self.assertEqual(abs(1234), builtins.abs(1234))
        self.assertEqual(abs(-1234), builtins.abs(1234))
        self.assertTrue(abs(-sys.maxsize-1) > 0)
        # float
        self.assertEqual(abs(0.0), builtins.abs(0.0))
        self.assertEqual(abs(3.14), builtins.abs(3.14))
        self.assertEqual(abs(-3.14), builtins.abs(3.14))
        # str
        self.assertRaises(TypeError, abs, 'a')
        # bool
        self.assertEqual(abs(True), 1)
        self.assertEqual(abs(False), 0)
        # other
        self.assertRaises(TypeError, abs)
        self.assertRaises(TypeError, abs, None)
