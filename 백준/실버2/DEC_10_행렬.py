""" 
https://www.acmicpc.net/problem/1080

행렬 

복습 

그리디 방식으로 접근 
- 다른 부분이 있다면 변경해주기. 
- 정당성?은 모르겠다. 

"""

import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
matrix = []
finalMatrix = []

for i in range(R):
    row = list(map(int, input().rstrip()))
    matrix.append(row)

for i in range(R):
    row = list(map(int, input().rstrip()))
    finalMatrix.append(row)


def countFlips():
    count = 0

    def flip33(r, c):
        for i in range(r, r+3):
            for j in range(c, c + 3):
                # math
                matrix[i][j] = 1 - matrix[i][j]

    # final check after flipping
    def checkEquality():
        for i in range(R):
            for j in range(C):
                if matrix[i][j] != finalMatrix[i][j]:
                    return False

        return True

    if len(matrix) < 3 or len(matrix[0]) < 3:
        print(-1)
        return

    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            # if found a difference in the location
            # flip everything in 3x3 dimensions
            if matrix[i][j] != finalMatrix[i][j]:
                flip33(i, j)
                count += 1

    if checkEquality():
        print(count)
    else:
        print(-1)


countFlips()
