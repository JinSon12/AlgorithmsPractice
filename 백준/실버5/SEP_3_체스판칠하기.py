"""
https://www.acmicpc.net/problem/1018

체스판 다시 칠하기 

반이 힌색이고 반이 검정이여야지만 valid chess board
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

grid = [(input().rstrip()) for _ in range(N)]

print(grid)


def findBW(r, c):
    nums1 = [0, 0]  # 1 = black, 0 = white RC = black
    nums2 = [0, 0]  # "" RC = white

    for i in range(r, r + 8):
        for j in range(c, c+8):
            # if grid[r][c] == "B":       # if we color first square as black,
            if i % 2 == 0:          # if row = even, then even col => B, odd col => W
                if j % 2 == 0:
                    if grid[i][j] != "B":   # 이곳이 검정이 아닌경우, 검정으로 칠할거다.
                        nums1[1] += 1
                    if grid[i][j] != "W":   # 이곳이 흰색이 아닌경우, 흰색으로 칠할거다.
                        nums2[0] += 1
                else:
                    if grid[i][j] != "W":
                        nums1[0] += 1
                    if grid[i][j] != "B":
                        nums2[1] += 1

            else:                   # if row == odd, then even col => W, odd col => B
                if j % 2 == 0:
                    if grid[i][j] != "W":
                        nums1[0] += 1
                    if grid[i][j] != "B":
                        nums2[1] += 1

                else:
                    if grid[i][j] != "B":
                        nums1[1] += 1
                    if grid[i][j] != "W":
                        nums2[0] += 1

    print(nums1, nums2)

    return min(sum(nums1), sum(nums2))

# 120 ms


def search(grid):
    minVal = 33

    for i in range(len(grid)-7):
        for j in range(len(grid[0])-7):
            temp = findBW(i, j)
            print("min,temp", minVal, temp, i, j)
            minVal = min(minVal, temp)

    return minVal


# faster, more concise method 107ms
def search_faster():
    M, N = map(int, input().split())

    board = []
    num_min = []
    for _ in range(M):
        board.append(input())

    for i in range(M-7):
        for j in range(N-7):
            num1 = 0
            num2 = 0
            for a in range(i, i+8):
                for b in range(j, j+8):
                    if (a+b) % 2 == 0:
                        if board[a][b] != 'W':
                            num1 += 1
                        else:
                            num2 += 1
                    else:
                        if board[a][b] != 'B':
                            num1 += 1
                        else:
                            num2 += 1
            num_min.append(num1)
            num_min.append(num2)

    print(min(num_min))


print(search(grid))

"""" 
8 8 
BBBBBBBW
BBBBBBBB
BBBBBBBW
BBBBBBBB
BBBBBBBW
BBBBBBBB
BBBBBBBW
BBBBBBBB
"""
