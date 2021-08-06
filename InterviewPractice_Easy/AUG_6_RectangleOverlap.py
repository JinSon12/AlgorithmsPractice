# https://leetcode.com/problems/rectangle-overlap/

"""
836. Rectangle overlap. 

"""

import timeit
from typing import List


class Solution:
    # 32ms, 58%
    def isRectangleOverlap_v1(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1x = [rec1[0], rec1[2]]
        rec1y = [rec1[1], rec1[3]]

        rec2x = [rec2[0], rec2[2]]
        rec2y = [rec2[1], rec2[3]]

        if rec2x[1] > rec1x[0] and rec2x[0] < rec1x[1] and rec2y[1] > rec1y[0] and rec2y[0] < rec1y[1]:
            return True

        elif rec1 == rec2:
            return True

    # v2_ without list
    def isRectangleOverlap_v2(self, rec1: List[int], rec2: List[int]) -> bool:

        if rec2[2] > rec1[0] and rec2[0] < rec1[2] and rec2[3] > rec1[1] and rec2[1] < rec1[3]:
            return True

        elif rec1 == rec2:
            return True

    # fastest and concise, 12ms

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # if 1 is left of 2
        # if 1 is below 2
        # if 1 is above 2
        # if 1 is right of 2
        if rec1[2] <= rec2[0]:
            return False
        if rec1[3] <= rec2[1]:
            return False
        if rec1[1] >= rec2[3]:
            return False
        if rec1[0] >= rec2[2]:
            return False
        return True


stn = Solution()
start1 = timeit.default_timer()
print(stn.isRectangleOverlap_v1([7, 8, 13, 15], [10, 8, 12, 10]))
stop1 = timeit.default_timer()
print('====== Time: for 1', stop1 - start1)

start = timeit.default_timer()
print(stn.isRectangleOverlap_v2([7, 8, 13, 15], [10, 8, 12, 10]))
stop = timeit.default_timer()
print('====== Time: for 2', stop - start)

start2 = timeit.default_timer()
print(stn.isRectangleOverlap_v2([7, 8, 13, 15], [10, 8, 12, 10]))
stop2 = timeit.default_timer()
print('====== Time: for 3', stop2 - start2)

start1 = timeit.default_timer()
print(stn.isRectangleOverlap_v1([7, 8, 13, 15], [10, 8, 12, 10]))
stop1 = timeit.default_timer()
print('====== Time: for 1', stop1 - start1)
