class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None

    def twoSumFaster(self, nums, target):
        """
        A faster variant of the algorithm using a hashmap where the addition is now O(n) instead of O(n2)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {num: index for index, num in enumerate(nums)}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums_dict and i != nums_dict[x]:
                return [i, nums_dict[x]]

        return None
