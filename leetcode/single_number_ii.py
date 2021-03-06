# https://leetcode.com/problems/single-number-ii/description/
# https://leetcode.com/articles/single-number-ii/ (Premium)


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num in seen:
                if seen[num] == 2:
                    del seen[num]
                else:
                    seen[num] += 1
            else:
                seen[num] = 1
        return seen.popitem()[0]


# same time as above: 36 ms, 100%
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen ={}
        for num in nums:
            if num in seen:
                if seen[num] == 2:
                    del seen[num]
                else:
                    seen[num] += 1
            else:
                seen[num] = 1
        return list(seen.keys())[0]
