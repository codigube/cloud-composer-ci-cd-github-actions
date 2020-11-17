import unittest

from utils import *

class TestUtils(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(say_hello('foo'), 'Hello foo!')

if __name__ == '__main__':
    unittest.main()