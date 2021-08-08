# https://leetcode.com/problems/fibonacci-number/

"""
509. Fibonacci Number

- DP problem

점화식 (Recurrence Formula):  
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

- Bottom up 
- Top Down 


어프로치 중 택 일. 

Bottom up 이 속도면에서 재귀 + lru Cache 보다 훨씬 더 빠르다. 

"""


class Solution:
    # 24 ms, 95%
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
