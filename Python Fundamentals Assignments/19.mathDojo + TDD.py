import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self
    
    def subtract(self, num, *nums):
        self.result -= num + sum(nums)
        return self
    
    def get_result(self):
        return self.result
    
class test(unittest.TestCase):
    # create an instance Before start testing
    def setUp(self):
        self.object_1 = MathDojo()

    def test_2_subtract(self):
        print("testcase2")
        self.assertEqual(self.object_1.subtract(3,2).get_result(),-5)
        self.assertEqual(self.object_1.subtract(-1).get_result(),-4)

    def test_1_add(self):
        print("testcase1")
        self.assertEqual(self.object_1.add(2).add(2,5,1).get_result(),10)
        self.assertEqual(self.object_1.add(-1,3,2).add(0).add(3,3).get_result(),20)
        self.assertEqual(self.object_1.subtract(3,2).get_result(),15)

if __name__ == '__main__':
    unittest.main() # this runs our tests
