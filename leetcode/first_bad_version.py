# https://leetcode.com/problems/first-bad-version/
# https://leetcode.com/articles/first-bad-version/


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n
        
        while first <= last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid - 1
            else:
                first = mid + 1
        return first


# 32 ms, 99.8%
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n

        while first <= last:
            mid = (first + last) // 2
            if isBadVersion(mid) == True:
                if isBadVersion(mid - 1) == False:
                    return mid
                last = mid - 1
            else:
                first = mid + 1