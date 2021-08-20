# https://leetcode.com/problems/binary-search/submissions/

""" 
KEY insight: 
- while loop 의 종료 시점
- left, right pointer 를 증가 시킬때 반드시 mid + 1 or mid - 1 하여 봤던 원소 재탐색 x 그리고 종료 조건 맞게. 
"""


class Solution:
    # 224ms, 96.7%
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # if there is no element in the list
        return -1
