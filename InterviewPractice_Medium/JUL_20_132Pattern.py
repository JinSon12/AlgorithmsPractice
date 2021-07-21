class Solution:
    def find132pattern_oN2(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            sec = nums[i]
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    if nums[j] < sec:
                        return True
                    elif nums[j] > sec:
                        sec = nums[j]
