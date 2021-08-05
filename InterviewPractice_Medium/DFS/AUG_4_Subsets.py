from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
print(stn.subsets([1, 2, 3]))
