"""
You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid. 
The car is supposed to get to the opposite, Northeast (top-right), corner of the grid. 
Given n, the size of the grid’s axes, write a function numOfPathsToDest that 
returns the number of the possible paths the driverless car can take.


For convenience, let’s represent every square in the grid as a pair (i,j). 
The first coordinate in the pair denotes the east-to-west axis, 
and the second coordinate denotes the south-to-north axis. 
The initial state of the car is (0,0), and the destination is (n-1,n-1).

The car must abide by the following two rules: 
it cannot cross the diagonal border. I
n other words, in every step the position (i,j) needs to maintain i >= j. 
See the illustration above for n = 5. 
In every step, it may go one square North (up), or one square East (right), 
but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,1).

Explain the correctness of your function, and analyze its time and space complexities.


DFS 
DP 
"""

# assume starting point is 0,0 -> n,n
from collections import deque
from functools import lru_cache


def num_of_paths(n):
    count = 0
    visited = set()
    res = []

    @lru_cache
    def dfs(r, c, pathSoFar):
        # termination condition
        if r == n-1 and c == n-1:
            res.append(pathSoFar[:])
            return 1

        elif r > n or c > n or r > r + 1:
            return 0

        top = right = 0
        if r + 1 >= c and (r+1, c) not in visited:
            visited.add((r+1, c))
            top = dfs(r + 1, c, pathSoFar + [[r+1, c]])
            visited.remove((r+1, c))
        if r >= c + 1 and (r, c + 1) not in visited:
            visited.add((r, c+1))
            right = dfs(r, c + 1, pathSoFar + [[r, c+1]])
            visited.remove((r, c+1))

        return top + right

    def recursiveCount(r, c):
        if r == 1 or c == 1:
            return 1

        return recursiveCount(r - 1, c) + recursiveCount(r, c - 1)

    count = [[-1 for x in range(n)] for y in range(n)]

    def recursiveMemo(r, c):
        if r < 0 or c < 0:
            return 0

        elif r < c:
            count[r][c] = 0

        elif count[r][c] != -1:
            return count[r][c]

        elif r == 0 and c == 0:
            count[r][c] = 1

        else:
            count[r][c] = recursiveMemo(r, c - 1) + recursiveMemo(r-1, c)

        return count[r][c]

    print(recursiveMemo(n-1, n-1))

    def dp(n): 
        if n == 1: 
            return 1 
        
        lastrow = [] 
        for i in range(1, n-1): 
            lastrow[i] = 1      # base case 
        
        currentRow = [] 
        for i in range(1, n-1): 
            for j in range(i, n-1): 
                if i == j: 
                    currentRow[i] = lastrow[i]
                
                else: 
                    currentRow[i] = currentRow[i-1] + lastrow[i]
                
                lastrow = currentRow    # update the lastrow with what is in currentRow, so that we have the most updated memoization



num_of_paths(4)
