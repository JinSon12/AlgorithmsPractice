"""
16926. 배열 돌리기. 

"""

import sys
input = sys.stdin.readline

R, C, K = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(R)]


def rotateGrid(grid, k):
    rlen = len(grid)    # row length
    clen = len(grid[0])  # col length
    layer = min(rlen, clen) // 2    # number of layers in the grid
    temp = []
    print(grid)

    for l in range(0, layer):
        r_end = rlen - l - 1
        c_end = clen - l - 1

        # top
        for i in range(l, c_end):
            temp.append(grid[l][i])

        # right
        for i in range(l, r_end):
            temp.append(grid[i][c_end])

        # bottom
        for i in range(c_end, l, -1):
            temp.append(grid[r_end][i])

        # left
        for i in range(r_end, l, -1):
            temp.append(grid[i][l])

        # print("temp", temp)

        # moving
        ind = 0
        # top
        for i in range(l, c_end):
            grid[l][i] = temp[(ind + k) % len(temp)]
            ind += 1

        # right
        for i in range(l, r_end):
            grid[i][c_end] = temp[(ind + k) % len(temp)]
            ind += 1

        # bottom
        for i in range(c_end, l, -1):
            grid[r_end][i] = temp[(ind + k) % len(temp)]
            ind += 1

        # left
        for i in range(r_end, l, -1):
            grid[i][l] = temp[(ind + k) % len(temp)]
            ind += 1

        temp = []
        # print("gird", grid)

    return grid


for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end=" ")
    print()
