import unittest
from lambda_function import my_func

class TestLambdaFunction(unittest.TestCase):

    def test_my_func_return_type(self):
        self.assertEqual(my_func('foo'), 'FOO')
    

if __name__ == '__main__':
    unittest.main()
