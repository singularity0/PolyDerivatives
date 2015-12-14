from derivative import Derivative
import unittest

class TestDerivative(unittest.TestCase):
    """docstring for TestDerivative"""
    def setUp(self):
        self.derivative = Derivative(1)

    def test_neshtosi(self):
        self.assertEqual(self.derivative.method, 2)



if __name__ == '__main__':
    unittest.main()