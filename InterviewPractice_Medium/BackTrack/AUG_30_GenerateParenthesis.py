"""
Generate Parenthesis 
https://leetcode.com/problems/generate-parentheses/

- DFS 
- 종료 조건에 대해서 생각해보기. 어떨때 ) 가 추가되어야 하는지 생각하기. 
- opening parenthesis 갯수가 n 보다 적을때 계속 오픈 추가 
- 클로징은 오픈 갯수보다 작을때만 추가할 수 있다. (즉, ")" 같은 케이스는 유효하지 않다 (open = 0, close = 1)) 


Key Insight: 
- 재귀호출, DFS 는 조건이 중요하다. 
- 반드시 종료 조건, 재귀를 하는 조건에 대해서 한번 더 생각해보기. 
"""


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # left = opening paren, right = closing
        def dfs(left, right, parenSoFar):
            if left > n or right > n:
                return

            # termination condition for invalid condition,
            if left < right:
                return

            #
            if left == n and left == right:
                res.append(parenSoFar[:])
                return

            # 이 조건이 있어야지 필요없이 재귀에 들어가지 않는다.
            # 만약에 없었다면, 재귀 호출이 한번 더 이루어지고, 그 함수 속에서 left > n 이 되어 종료.
            # 즉 필요없이 재귀호출이 되는 것.
            if left < n:
                # add one more opening
                dfs(left + 1, right, parenSoFar + "(")

            if right < left:
                # add one more closing
                dfs(left, right + 1, parenSoFar + ")")

        dfs(0, 0, "")

        return res

    def generateParenthesis_faster(self, n: int) -> List[str]:
        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()

        return ans


stn = Solution()
stn.generateParenthesis(3)
