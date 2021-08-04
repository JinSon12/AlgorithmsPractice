# https://leetcode.com/problems/combinations/


"""
77. Combinations


"""


class Solution:
    # 448ms, 70% faster
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(elements, start, k):
            # 종료 조건. k == 0
            if k == 0:
                res.append(elements[:])  # 반드시 슬라이싱으로 카피해주어야지 참조값이 저장되지 않는다.

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return res
