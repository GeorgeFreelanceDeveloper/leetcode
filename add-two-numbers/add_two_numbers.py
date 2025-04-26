# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []
        sliding_number = 0

        item_a = l1
        item_b = l2

        while item_a is not None or item_b is not None:
            a = item_a.val if item_a is not None else 0
            b = item_b.val if item_b is not None else 0
            sub_result = a + b + sliding_number

            if sub_result >= 10:
                sliding_number = 1
                result.append(sub_result - 10)
            else:
                sliding_number = 0
                result.append(sub_result)

            item_a = item_a.next if item_a is not None else None
            item_b = item_b.next if item_b is not None else None

        if sliding_number == 1:
            result.append(1)

        result_list = None
        for x in reversed(result):
            result_list = ListNode(val=x, next=result_list)
        return result_list

    def addTwoNumbersFaster(self, l1, l2):
        # TODO: implement me
        pass