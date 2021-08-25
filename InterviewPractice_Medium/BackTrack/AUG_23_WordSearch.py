"""


"""
from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, ind):
            res = False
            temp = board[r][c]
            board[r][c] = 0

            if ind == len(word)-1:
                return True

            for x, y in dir:
                newr = r + x
                newc = c + y

                if 0 <= newr < len(board) and 0 <= newc < len(board[0]) and board[newr][newc] == word[ind+1]:
                    res = dfs(newr, newc, ind+1)
                    if res:  # 한 군데라도 True (원하는 단어를 찾았을때,) 이면 단어가 있다는 뜻: 따라서 True return
                        return res

            board[r][c] = temp  # 다시 원래 값으로 바꾸어 주기.
            return res

        ind = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[ind]:
                    found = dfs(i, j, 0)
                    if found:
                        return True

        return False


# Clean, fast, concise (16ms)
class Solution_v2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w = len(word)

        if w > m*n:
            return False

        counts = Counter(word)
        needed = len(counts)
        found = 0

        for row in board:
            for c in row:
                if c in counts and counts[c] > 0:
                    counts[c] -= 1
                    if counts[c] == 0:
                        found += 1
                        if found == needed:
                            break

        if found < needed:
            return False
        # 전처리 완료. (필요한 단어수와 존재하는 글자수 비교)

        def backtrack(i, j, k):
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[k]:
                return False

            if k == w-1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'
            res = backtrack(i+1, j, k+1) \
                or backtrack(i-1, j, k+1) \
                or backtrack(i, j+1, k+1) \
                or backtrack(i, j-1, k+1)
            board[i][j] = tmp

            return res

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False
