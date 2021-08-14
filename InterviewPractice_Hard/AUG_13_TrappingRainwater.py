"""
42. Trapping Rain Water

Key Insight 
- From the current index (pillar), find the highest value on its left and the highest value from its right. 
- the current index's water amount = min(left_highest, right_highest) - current_height

- brute force O(n^2)
- DP o(N) - using extra ds (arrays) to store the highest height for each index for the left side and the right side. 

https://www.geeksforgeeks.org/trapping-rain-water/
"""


class Solution:
    def trap_bruteForce(self, height: List[int]) -> int:
        res = 0

        for i in range(1, len(height)-1):
            maxLeft = height[i]
            maxRight = height[i]

            for j in range(0, i):
                maxLeft = max(height[j], maxLeft)

            for j in range(i, len(height)):
                maxRight = max(height[j], maxRight)

            res += min(maxLeft, maxRight) - height[i]

            # print(i, maxLeft, maxRight, res)

        return res

    def trap_DP(self, height: List[int]) -> int:
        W = len(height)
        res = 0

        left = [0] * W
        right = [0] * W

        left[0] = height[0]
        right[W-1] = height[W-1]

        for i in range(1, W):
            left[i] = max(left[i-1], height[i])

        for i in range(W - 2, -1, -1):
            right[i] = max(right[i+1], height[i])

        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]

        return res
