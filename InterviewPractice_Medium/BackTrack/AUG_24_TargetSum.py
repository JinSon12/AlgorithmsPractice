from typing import List
from functools import lru_cache


def findTargetSumWays(nums: List[int], target: int) -> int:
    resA = []

    @lru_cache  # leetcode 에서는 cache 로 하기.
    def dfs(total, pos, count):
        res = 0
        # termination condition
        if total == target and pos == len(nums):
            resA.append(count[:])
            return 1
        elif pos == len(nums):
            return 0

        temp = nums[pos]

        if pos + 1 <= len(nums):
            res = dfs(total + nums[pos], pos+1, count + [nums[pos]]) + \
                dfs(total - nums[pos], pos+1, count + [nums[pos]*-1])

        nums[pos] = temp
        return res

    count = dfs(0, 0, [])

    print(resA)
    return count


print(findTargetSumWays([1, 0], 1))
