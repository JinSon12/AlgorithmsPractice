from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    visited = set({})

    def dfs(r, c):
        if r < 0 or r > len(board) - 1 or c < 0 or c > len(board[0]) - 1 or board[r][c] != "O":
            return

        visited.add((r, c))
        board[r][c] = "#"

        # for loop 을 사용하면 더 느리다.
        # 그냥 일일이 적는것이 좀 더 빠르게 된다.
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            dfs(r + x, c + y)

    # visit O that are only on the border.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0 or i == len(board) - 1:
                dfs(i, j)
            if j == 0 or j == len(board[0]) - 1:
                dfs(i, j)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                board[i][j] == "X"
            elif board[i][j] == "#":
                board[i][j] = "O"

    # 위 for loop 에 if-elif 을 사용함으로써, 더이상 visited 가 필요가 없어졌다.
    # for r, c in visited:
    #     board[r][c] = "O"

# board = [["O", "O", "O", "O", "X", "X"], ["O", "O", "O", "O", "O", "O"], ["O", "X", "O", "X", "O", "O"], [
#     "O", "X", "O", "O", "X", "O"], ["O", "X", "O", "X", "O", "O"], ["O", "X", "O", "O", "O", "O"]]


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
solve(board)

print("+++++++")

for i in range(len(board)):
    print(board[i])
