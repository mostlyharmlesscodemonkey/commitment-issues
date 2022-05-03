
# unit tests

# import code to test
import dummy
import unittest

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(dummy.increment(3), 4)
    
    def test_decrement(self):
        self.assertEqual(dummy.decrement(3), 2)

if __name__ == '__main__':
    unittest.main()