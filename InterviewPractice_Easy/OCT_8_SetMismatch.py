"""
Set Mismatch

"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        setN = set(nums)
        
        
        res = [] 
        
        j = 0
        nums.sort()
        for i in range(1, len(nums)): 
            if nums[j] == nums[i]: 
                res.append(nums[i])
            j += 1 
        
        for i in range(1, len(nums) + 1): 
            if i not in setN: 
                res.append(i)
        
        return res
        
                