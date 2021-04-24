# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int = length of the array 
        """
        # we must keep have O(1) extra memory , hashSet 
        numSize = len(nums)
        for i in range(1, numSize) : 
            if nums[(i-1)] == nums[i] : 
                del nums[i-1]
                i -= 1 
                numSize -= 1 
        return len(nums)
                
        