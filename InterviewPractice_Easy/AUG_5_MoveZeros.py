# https://leetcode.com/problems/move-zeroes/

import timeit
from typing import List

"""
238. Move Zeros 


"""


class Solution:
    # 32 ms
    def moveZeroes_v1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, 1

        while end < len(nums):
            if nums[end] != 0 and nums[start] == 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
            elif nums[start] != 0:
                start += 1

            end += 1

    # 28ms
    def moveZeroes_fastest(self, nums: List[int]) -> None:
        last_idx = 0
        for i in nums:
            if i != 0:
                nums[last_idx] = i
                last_idx += 1
        for i in range(last_idx, len(nums)):
            nums[i] = 0


stn = Solution()
start = timeit.default_timer()
print(stn.moveZeroes_v1([0, 1, 0, 3, 12]))
stop = timeit.default_timer()
print('Time: for 1', stop - start)

start = timeit.default_timer()
print(stn.moveZeroes_fastest([0, 1, 0, 3, 12]))
stop = timeit.default_timer()
print('Time: for backtracking', stop - start)
