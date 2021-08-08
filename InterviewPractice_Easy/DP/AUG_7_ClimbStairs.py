# https://leetcode.com/problems/climbing-stairs/

"""
70. Climbing Stairs

- DP Problem
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0, 1, 2]

        for i in range(3, n+1):
            temp = dp[i - 1] + dp[i - 2]
            dp.append(temp)

        return dp[n]
