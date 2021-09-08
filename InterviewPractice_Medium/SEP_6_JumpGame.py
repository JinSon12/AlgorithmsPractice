"""
Jump Game

https://leetcode.com/problems/jump-game/

1. Backtracking (TLE)
2. DP 
3. Greedy

"""


from collections import deque
from typing import List
from functools import lru_cache


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastInd = len(nums) - 1
        visited = set([0])

        def dfs(i):
            print(i)
            if i >= lastInd:
                return True

            # if nums[i] == 0:
            #     return False

            val = nums[i]
            res = False
            for j in range(val, 0, -1):
                # print(j + 1 + i, i)
                if j+i < len(nums) and nums[j+i] == 0:
                    res = False
                elif j+i not in visited:
                    res = dfs(j+i)
                if res == True:
                    return True

            return res

        return dfs(0)

    # 3000ms
    def canJump_cleaner(nums):
        visited = set()

        @cache
        def dfs(ind):
            # termination condition
            if ind >= len(nums):
                return True

            if ind in visited:
                return False

            val = nums[ind]
            res = False
            for dist in range(val, 0, -1):
                if ind + dist not in visited:
                    res = dfs(dist + ind)
                    visited.add(dist+ind)
                    if res:
                        return True

    def canJump_greedy(self, nums: List[int]) -> bool:
        lastInd = len(nums) - 1
        max_dist = 0

        for i in range(len(nums)):
            max_dist = max(nums[i] + i, max_dist)
            if max_dist >= lastInd:
                # print(max_dist)
                return True

            if nums[i] == 0 and max_dist <= i:
                return False

    def canJump_DP(self, nums: List[int]) -> bool:
        dp = [False for i in range(len(nums))]
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] == True and (i-j) <= nums[j]:
                    dp[i] = True
                    break

        return dp[len(nums) - 1]

    # 7000ms
    def canJump_bfs(self, nums: List[int]) -> bool:
        queue = deque([0])
        seen = set([0])

        while queue:
            index = queue.popleft()
            if index == len(nums) - 1:
                return True
            if nums[index] + index > len(nums):
                return True
            for i in range(nums[index]+1):
                jmp = index + i
                if jmp not in seen:
                    queue.append(jmp)
                    seen.add(jmp)

        return False


stn = Solution()
print(stn.canJump([2, 3, 1, 1, 4]))
