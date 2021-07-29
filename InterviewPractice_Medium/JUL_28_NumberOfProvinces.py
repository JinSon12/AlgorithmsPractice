from typing import List

# https://leetcode.com/problems/number-of-provinces/
# 547. Number of Provinces


class Solution:

    # very slow, 372ms, 7.44%
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                # print("j change", i, j)
                if isConnected[i][j] == 1:
                    # print("isconnected")
                    self.dfs(isConnected, j)
                    count += 1

        return count

    def dfs(self, isConnected, j):
        for i in range(len(isConnected[j])):
            if isConnected[j][i] == 1:
                isConnected[j][i] = 0
                self.dfs(isConnected, i)

    def findCircleNum_faster_v2(self, isConnected: List[List[int]]) -> int:

        visited = [0 for _ in range(len(isConnected))]
        provinces = 0
        for i in range(len(isConnected)):
            if visited[i] == 0:
                self.isProvince(isConnected, visited, i)
                provinces += 1
        return provinces

    def isProvince(self, isConnected: List[List[int]], visited: List[bool], row) -> bool:
        # print(isConnected)
        for j in range(len(isConnected[0])):
            if isConnected[row][j] and visited[j] == 0:
                visited[j] = 1
                self.isProvince(isConnected, visited, j)

        return True

    def findCircleNum_iterative(self, matrix: List[List[int]]) -> int:
        vis = set()
        count = 0
        queue = collections.deque()

        for i in range(len(matrix)):
            if i not in vis:
                queue = collections.deque()
                queue.append(i)
                vis.add(i)

                while len(queue) != 0:
                    item = queue.popleft()

                    for j in range(len(matrix)):
                        if j not in vis and matrix[item][j] == 1:
                            queue.append(j)
                            vis.add(j)
                count += 1

        return count

    # faster solution, 180ms, 92%
    def findCircleNum_v2(self, isConnected: List[List[int]]) -> int:
        count = 0
        seen = set()

        def dfs(isConnected, j):
            for i in range(len(isConnected[j])):  # takes in length of row
                # w/o isConnected[row][col] == 1,
                # then it would just add all the i's
                # and consider it as one graph (although they might not be connected)
                if i not in seen and isConnected[j][i] == 1:
                    isConnected[j][i] = 0
                    seen.add(i)
                    dfs(isConnected, i)

        for i in range(len(isConnected)):
            if i not in seen:
                dfs(isConnected, i)
                count += 1

        return count


stn = Solution()
print(stn.findCircleNum_v2(
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
