# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        # indices to store the left most, and the right most indices
        # where the target number appears.
        LInd, RInd = -1, -1

        if nums is None:
            return (-1, -1)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                LInd = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                RInd = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return (LInd, RInd)

    def searchRangeV2_faster(self, nums: List[int], target: int) -> List[int]:

        l = self.searchLeft(nums, target)
        r = self.searchRight(nums, target)
        if l <= r:
            return [l, r]
        else:
            return [-1, -1]

    def searchLeft(self, nums, target):  # search for staring index
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            # nums[mid]>=target: range starts at the left of mid
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def searchRight(self, nums, target):  # search for ending index
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r
