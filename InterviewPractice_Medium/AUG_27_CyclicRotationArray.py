"""
1914. Cyclically Rotating a Grid 

https://leetcode.com/problems/cyclically-rotating-a-grid/

1) DFS 
2) temp array + ordered saving elements 
3) queue + rotate 

복습 
queue + rotate 로도 해보기 .

"""
from typing import List


class Solution:
    # 140 ~ 230ms
    def rotateGrid_v1(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rlen = len(grid)    # row length
        clen = len(grid[0])  # col length
        layer = min(rlen, clen) // 2    # number of layers in the grid
        temp = []

        for l in range(0, layer):
            r_end = rlen - l - 1
            r_st = l
            c_st = l
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
                print(grid)

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

    # using queue.
    def rotateGrid_v2(self, grid: List[List[int]], k: int) -> List[List[int]]:
        pass

    # 모범답안
    def rotateGrid_answer(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        i, j = 0, 0
        bottom, right = n-1, m-1
        while i < n//2 and j < m//2:
            temp = []
            for x in range(j, right):
                temp.append(grid[i][x])
            for x in range(i, bottom):
                temp.append(grid[x][right])
            for x in range(right, j, -1):
                temp.append(grid[bottom][x])
            for x in range(bottom, i, -1):
                temp.append(grid[x][j])

            indx = 0
            for x in range(j, right):
                grid[i][x] = temp[(k + indx) % len(temp)]
                indx += 1
            for x in range(i, bottom):
                grid[x][right] = temp[(k + indx) % len(temp)]
                indx += 1
            for x in range(right, j, -1):
                grid[bottom][x] = temp[(k + indx) % len(temp)]
                indx += 1
            for x in range(bottom, i, -1):
                grid[x][j] = temp[(k + indx) % len(temp)]
                indx += 1

            i += 1
            j += 1
            bottom -= 1
            right -= 1
        return grid


stn = Solution()
stn.rotateGrid_v1([[1, 2, 3, 4], [5, 6, 7, 8], [
                  9, 10, 11, 12], [13, 14, 15, 16]], 1)
