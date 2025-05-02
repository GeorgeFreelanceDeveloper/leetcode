class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # if len(s) == 1:
        #     return 1
        #
        # if len(s) == 2:
        #     if s[0] == s[1]:
        #         return 1
        #     else:
        #         return 2

        max_length = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                duplicates = (len(set(substring))) != len(substring)
                if duplicates:
                    break
                elif len(substring) > max_length:
                    max_length = len(substring)

        return max_length

    def contains_duplicates_slower(self, substring):
        if len(substring) == 1:
            return False

        if len(substring) == 2:
            if substring[0] == substring[1]:
                return True
            else:
                return False

        duplicates = False
        for letter in substring:
            if substring.count(letter) > 1:
                duplicates = True
        return duplicates

    def contains_duplicates_faster(self, substring):
        return (len(set(substring))) != len(substring)