# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def mergeV_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums2_ind = 0

        for i in range(len(nums1)):
            if nums1[i] == 0 and nums2_ind < len(nums2):
                nums1[i] = nums2[nums2_ind]
                nums2_ind += 1

        return nums1.sort()
