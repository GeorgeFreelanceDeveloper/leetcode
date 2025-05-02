import unittest
from longest_substring_without_repeating_characters import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):

    def setUp(self):
        pass

    def test_example_1(self):
        input = 'abcabcbb'
        # input = 'aab'
        expected_result = 3

        self.assertEqual(expected_result, Solution.lengthOfLongestSubstring(self, input))

    def test_example_2(self):
        input = 'bbbbb'
        expected_result = 1

        self.assertEqual(expected_result, Solution.lengthOfLongestSubstring(self, input))

    def test_example_3(self):
        input = 'pwwkew'
        expected_result = 3

        self.assertEqual(expected_result, Solution.lengthOfLongestSubstring(self, input))

    def test_example_4(self):
        input = 'a'
        expected_result = 1

        self.assertEqual(expected_result, Solution.lengthOfLongestSubstring(self, input))

    def test_example_5(self):
        input = 'ydfatmztyqgmuxjedlxcaftgflhuqldooiqjxqfvinjcksgqeguglnosavorgrhxcaizsnwabfcnalfgrzmepaypxniegsdisljk'
        expected_result = 12

        self.assertEqual(expected_result,Solution.lengthOfLongestSubstring(self,input))
