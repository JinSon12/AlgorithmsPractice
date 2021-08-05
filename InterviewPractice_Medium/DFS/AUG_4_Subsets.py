from typing import List
import timeit

# https://leetcode.com/problems/subsets/

"""
78. Subsets 

Key Insights: 
- Combinations problem 과 매우 유사. 
- Recursively search for all the possible subsets 
- second function for backtracking

"""


class Solution:

    # slower, due to for loop
    def subsets_v1(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(ind, subsetSoFar):
            res.append(subsetSoFar)

            for i in range(ind, len(nums)):
                dfs(i + 1, subsetSoFar + [nums[i]])

        dfs(0, [])

        return res

    def subsets_backtracking(self, nums: List[int]) -> List[List[int]]:
        res = []

        numbers = []

        def dfs(i=0):
            if i == len(nums):
                res.append(numbers.copy())
                return

            numbers.append(nums[i])
            dfs(i + 1)
            numbers.pop()
            dfs(i + 1)

        dfs()

        return res


stn = Solution()

start = timeit.default_timer()
print(stn.subsets_v1([1, 2, 3]))
stop = timeit.default_timer()
print('Time: for 1', stop - start)

start = timeit.default_timer()
print(stn.subsets_backtracking([1, 2, 3]))
stop = timeit.default_timer()
print('Time: for backtracking', stop - start)
