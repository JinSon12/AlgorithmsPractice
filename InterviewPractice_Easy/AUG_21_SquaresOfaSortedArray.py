"""
https://leetcode.com/problems/squares-of-a-sorted-array/

977. Squares of a Sorted Array 

detailed explanation for two pointer approach: 
https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator

- start from 0, len(nums) - 1 
- compare 
- bigger number pointer + 1 혹은 -1 하기. 

복습 요
"""

from collections import deque


class Solution:
    # 1st approach, very slow. (n*logn time)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]

            nums[i] = num ** 2

        return sorted(nums)

    # no new res, but not in place anymore (fastest solution)
    def sortedSquares_notInPlace(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            res.append(num * num)

        res.sort()

        return res

    def sortedSquares(self, nums: List[int]) -> List[int]:
        d = deque(nums)
        res = []

        while d:
            l = d[0] ** 2
            r = d[-1] ** 2

            if l > r:

                res.append(l)
                d.popleft()

            else:
                res.append(r)
                d.pop()

        return res[::-1]
