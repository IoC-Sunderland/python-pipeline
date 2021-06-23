import unittest
from test import my_func

class TestStringMethods(unittest.TestCase):

    def test_test_file(self):
        self.assertEqual(my_func('foo'), 'FOO')
    

if __name__ == '__main__':
    unittest.main()
