# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while (left <= right):
            mid = (left + right) // 2

            # mid 가 bad version:
            # mid 나 mid 전부터 bad version
            if isBadVersion(mid):
                right = mid - 1

            # mid 가 bad version 이 아닐 경우:
            # mid 이후로부터 bad version
            else:
                left = mid + 1

        return left


def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 1, n

    while (left <= right):
        mid = (left + right) // 2

        if mid == True:
            return mid


firstBadVersion(5)
