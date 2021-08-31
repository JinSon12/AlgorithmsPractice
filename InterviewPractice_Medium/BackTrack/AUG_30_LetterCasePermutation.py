""" 
https://leetcode.com/problems/letter-case-permutation/

Letter Case Permutation 

- DFS / BFS 

Key Insight: 
- Recursion 조건 더 생각하기. 
- 트리를 그려보면서 조건을 생각하기. 
- 여기서는 
  1) 글자가 숫자일 경우 
  2) 숫자가 아닐 경우 
      1) 대문자일 경우 -> 소 (swapcase() 함수 사용하기.)
      2) 소문자일 경우 -> 대 
  후 인덱스 스킵하기. 

즉, 이 부분이 핵심 로직. 
  # for changing the case
    if not s[pos].isnumeric():
        dfs(pos + 1, st + s[pos].swapcase())

  # normal
    dfs(pos + 1, st + s[pos])
  
"""


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        numeric = True
        for i in s:
            if not i.isnumeric():
                numeric = False

        def dfs(pos, st):
            # termination condition
            if pos == len(s):
                res.append(st)
                return

            # for changing the case
            if not s[pos].isnumeric():
                dfs(pos + 1, st + s[pos].swapcase())

            # normal
            dfs(pos + 1, st + s[pos])

        if not numeric:
            dfs(0, "")
        else:
            res.append(s)

        return set(res)
