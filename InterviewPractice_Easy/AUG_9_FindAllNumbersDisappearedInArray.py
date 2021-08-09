# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

"""
448. Find All Numbers Disappeared in an Array


"""

import timeit
from typing import List


class Solution:
    # faster, more concise,
    # less memory
    def findDisappearedNumbers_faster(self, nums: List[int]) -> List[int]:
        numset = set(nums)
        print(numset)
        res = []

        for i in range(1, len(nums)+1):
            if i not in numset:
                res.append(i)

        return res

    # 332 ~ 356ms 84 ~ 60%
    # uses more memory
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numset = ({x + 1 for x in range(len(nums))})

        for i in set(nums):
            if i in numset:
                numset.remove(i)

        return list(numset)


stn = Solution()
start = timeit.default_timer()
stn.findDisappearedNumbers_faster([4, 3, 2, 7, 8, 2, 3, 1])
stop = timeit.default_timer()
print('Time: ', stop - start)
