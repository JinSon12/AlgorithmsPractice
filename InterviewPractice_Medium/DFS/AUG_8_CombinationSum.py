# https://leetcode.com/problems/combination-sum/

"""
39. Combination Sum

Key Insight 
- DFS 

"""


class Solution:
    # 80ms, 60%
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(ind, currTotal, elSoFar):

            # 종료 조건
            if currTotal <= 0:
                if currTotal == 0:
                    res.append(elSoFar)
                return

            for i in range(ind, len(candidates)):
                dfs(i, currTotal - candidates[i], elSoFar + [candidates[i]])

        res = []

        # 이때, 모든 원소를 traverse 하는 for loop 사용하지 않는다.
        # 한번의 dfs 가 ind로 부터 찾을 수 있는 모든 path 를 찾을 것이다.
        dfs(0, target, [])

        return res
