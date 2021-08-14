"""
14719. 빗물

"""

import sys
input = sys.stdin.readline

H, W = map(int, input().strip().split())

height = list(map(int, input().strip().split()))


# 128ms
def trap_bruteForce(height):
    res = 0

    for i in range(1, len(height)-1):
        maxLeft = height[i]
        maxRight = height[i]

        for j in range(0, i):
            maxLeft = max(height[j], maxLeft)

        for j in range(i, len(height)):
            maxRight = max(height[j], maxRight)

        res += min(maxLeft, maxRight) - height[i]

        # print(i, maxLeft, maxRight, res)

    return res


# precompute the highest point for each index.
# first and last pillars would be naturally ignored due to min(left, right) - height.
# 80ms
def trap_dp(height):
    res = 0

    left = [] * W  # = len(height)
    right = [] * W  # = len(height)

    left.append(height[0])
    right[W-1] = height[W-1]

    for i in range(1, len(height)):
        left[i] = max(left[i-1], height[i])

    for i in range(len(height) - 2, -1, -1):
        right[i] = max(right[i+1], height[i])

    for i in range(len(height)):
        res += min(left[i], right[i]) - height[i]

    return res


def trap_dfs(height):
    def left_dfs(board):
        if len(board) <= 1:
            return 0
        big_score = max(board)
        big_point = max(
            list(filter(lambda x: board[x] == big_score, range(len(board)))))
        if big_score == 0:
            return 0

        rain_sum = 0
        for i in range(big_point + 1, len(board)):
            rain_sum += big_score - board[i]
        return rain_sum + left_dfs(board[:big_point])

    def right_dfs(board):
        if len(board) <= 1:
            return 0
        big_score = max(board)
        big_point = min(
            list(filter(lambda x: board[x] == big_score, range(len(board)))))
        if big_score == 0:
            return 0

        rain_sum = 0
        for i in range(0, big_point):
            rain_sum += big_score - board[i]
        return rain_sum + right_dfs(board[big_point + 1:])

    m_point = M.index(max(M))
    left_sum = left_dfs(M[:m_point])
    right_sum = right_dfs(M[m_point+1:])
    print(left_sum + right_sum)


print(trap_bruteForce(height))
