# https://leetcode.com/problems/two-sum/
"""
Two sum

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            if nums[i] in vals:
                return [vals[nums[i]], i]

            vals[target - nums[i]] = i

# two sum revisited


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # k : target - nums[i], v : ind cur nums[i]
        dn = {}

        for i in range(len(nums)):
            if nums[i] in dn:
                return [i, dn[nums[i]]]
            dn[target - nums[i]] = i
