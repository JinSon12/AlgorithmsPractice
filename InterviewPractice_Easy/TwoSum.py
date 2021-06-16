# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            if nums[i] in vals:
                return [vals[nums[i]], i]

            vals[target - nums[i]] = i
