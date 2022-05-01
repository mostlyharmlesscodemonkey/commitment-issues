
# unit tests

# import code to test
import app
import unittest

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(app.increment(3), 4)
    
    def test_decrement(self):
        self.assertEqual(app.decrement(3), 2)

if __name__ == '__main__':
    unittest.main()