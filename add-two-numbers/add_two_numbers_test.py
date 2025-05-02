import unittest
from add_two_numbers import Solution
from add_two_numbers import ListNode

class TestAddTwoNumbers(unittest.TestCase):

    def test_example_1(self):
        l1 = self.list_to_linked_list([2,4,3])
        l2 = self.list_to_linked_list([5,6,4])
        expected_result = [7,0,8]
        self.assertEqual(expected_result, self.linked_list_to_list(Solution.addTwoNumbers(self, l1, l2)))

    def test_example_2(self):
        l1 = self.list_to_linked_list([0])
        l2 = self.list_to_linked_list([0])
        expected_result = [0]
        self.assertEqual(expected_result, self.linked_list_to_list(Solution.addTwoNumbers(self, l1, l2)))

    def test_example_3(self):
        l1 = self.list_to_linked_list([9,9,9,9,9,9,9])
        l2 = self.list_to_linked_list([9,9,9,9])
        expected_result = [8,9,9,9,0,0,0,1]
        self.assertEqual(expected_result, self.linked_list_to_list(Solution.addTwoNumbers(self, l1, l2)))

    def list_to_linked_list(self, lst):
        if not lst:
            return None

        head = ListNode(lst[0])
        current = head

        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next

        return head

    def linked_list_to_list(self, head):
        result = []
        current = head

        while current:
            result.append(current.val)
            current = current.next

        return result