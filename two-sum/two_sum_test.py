import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):

    def setUp(self):
        pass

    def test_example_1(self):
        nums = [2,7,11,15]
        target = 9
        expected_result = [0,1]

        self.assertEqual(expected_result, Solution.twoSum(self, nums, target))
        self.assertEqual(expected_result, Solution.twoSumFaster(self, nums, target))

    def test_example_2(self):
        nums = [3,2,4]
        target = 6
        expected_result = [1, 2]

        self.assertEqual(expected_result, Solution.twoSum(self, nums, target))
        self.assertEqual(expected_result, Solution.twoSumFaster(self, nums, target))

    def test_example_3(self):
        nums = [3,3]
        target = 6
        expected_result = [0, 1]

        self.assertEqual(expected_result, Solution.twoSum(self, nums, target))
        self.assertEqual(expected_result, Solution.twoSumFaster(self, nums, target))

if __name__ == '__main__':
    unittest.main()