# https://leetcode.com/problems/search-insert-position/submissions/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while(left <= right):
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # when you exit while loop,
        # the condition must be left > right.
        # the position of the left is where the element can be inserted.
        return left


def findMed(nums, target):
    left, right = 0, len(nums)-1

    while(left <= right):
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # while loop 를 exit 했을때는 left > right.
    print(left, "  ", right)


findMed([1, 3, 5, 6], 0)
