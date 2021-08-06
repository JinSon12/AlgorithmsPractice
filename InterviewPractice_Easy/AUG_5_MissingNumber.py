# https://leetcode.com/problems/missing-number/

"""
268. Missing Number

Key Insight: 
- Set lookup -> O(1)
- list lookup -> O(n)

"""


class Solution:
    # 120ms
    def missingNumber(self, nums: List[int]) -> int:
        sNums = set(nums)

        for i in range(len(nums) + 1):
            if i not in sNums:
                return i

    # 2550ms
    def missingNumber_listLookup(self, nums: List[int]) -> int:
        sNums = set(nums)

        for i in range(len(nums) + 1):
            if i not in sNums:
                return i
