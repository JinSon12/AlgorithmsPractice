"""
https://leetcode.com/problems/pacific-atlantic-water-flow/

"""


from typing import List, Tuple, overload
from queue import Queue
from enum import Enum
from typing import List

"""
# runtime => 4^n

현재는 모든 지점에서 dfs 를 하기 때문에 recursionLimit 에 걸릴 확률이 높다 

"""


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    toPacific = [[0 for i in range(len(heights[0]))]
                 for _ in range(len(heights))]

    toAtlantic = [[0 for i in range(len(heights[0]))]
                  for _ in range(len(heights))]

    pacVisited = [[False for _ in range(len(heights[0]))]
                  for _ in range(len(heights))]

    atVisited = [[False for _ in range(len(heights[0]))]
                 for _ in range(len(heights))]

    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    result = []

    def pacDFS(row, col):
        if row == 0 or col == 0:
            return True

        pacVisited[row][col] = True

        res = False
        for dir in dirs:
            newR = row + dir[0]
            newC = col + dir[1]

            if 0 < newR < len(heights) and 0 < newC < len(heights[0]) and pacVisited[newR][newC] == False:
                # height 조건 확인
                if heights[newR][newC] < heights[row][col]:
                    res = pacDFS(newR, newC)
                    if res:
                        return True

        return res

    def AtDFS(row, col):
        # ! 왜 틀린지 알아보기
        # if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]):
        #     return False

        # ! row == len(heights) -> row == len(heights) - 1 으로 변경.
        if row == len(heights) - 1 or col == len(heights[0]) - 1:
            return True

        atVisited[row][col] = True

        res = False
        # height checking
        for dir in dirs:
            newR = row + dir[0]
            newC = col + dir[1]

            if 0 < newR < len(heights) and 0 < newC < len(heights[0]) and atVisited[newR][newC] == False:

                if heights[newR][newC] <= heights[row][col]:
                    res = AtDFS(newR, newC)
                    if res:
                        return True

        return res

    # visited 배열은 따로 필요가 없다.
    # 어느 길로 가던 도착만 하면 됨.
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            pacVisited = [[False for _ in range(len(heights[0]))]
                          for _ in range(len(heights))]

            atVisited = [[False for _ in range(len(heights[0]))]
                         for _ in range(len(heights))]

            resPacDFS = pacDFS(i, j)
            resAtDFS = AtDFS(i, j)

            if resPacDFS:
                toPacific[i][j] = 1

            if resAtDFS:
                toAtlantic[i][j] = 1

            if resPacDFS and resAtDFS:
                result.append([i, j])

    print(toAtlantic, "atlantic, pacific", toPacific)
    print(result)


"""

v1 과는 다른 점: 

모든 지점에서 dfs 를 하지 않아도 된다. 
물에 직접 닿는 지점에서 dfs 하면서 도달 할 수 있는 곳을 확인한다. 
예) pacific 에 닿는 지점에서 출발해서 도달 할 수 잇는 곳을 찾는다 
   atlantic 에 닿는 지점에서 출발해서 도달 할 수 있는 곳을 찾는다. 

"""


def pacificAtlantic_v2(heights: List[List[int]]) -> List[List[int]]:
    # toPacific = [[0 for i in range(len(heights[0]))]
    #              for _ in range(len(heights))]

    # toAtlantic = [[0 for i in range(len(heights[0]))]
    #               for _ in range(len(heights))]

    pacVisited = [[False for _ in range(len(heights[0]))]
                  for _ in range(len(heights))]

    atVisited = [[False for _ in range(len(heights[0]))]
                 for _ in range(len(heights))]

    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    result = []

    def pacDFS(row, col):
        pacVisited[row][col] = True

        res = False
        for dir in dirs:
            newR = row + dir[0]
            newC = col + dir[1]

            if 0 <= newR < len(heights) and 0 <= newC < len(heights[0]) and pacVisited[newR][newC] == False:
                # height 조건 확인
                if heights[newR][newC] >= heights[row][col]:
                    res = pacDFS(newR, newC)
                    if res:
                        return True

        return res

    def AtDFS(row, col):
        # ! 왜 틀린지 알아보기 :: 왜냐, 범위 확인은 이미 dir for loop 안에서 해결된다.
        # if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]):
        #     return False

        # ! row == len(heights) -> row == len(heights) - 1 으로 변경.
        # if row == len(heights) - 1 or col == len(heights[0]) - 1:
        #     return True

        atVisited[row][col] = True

        res = False
        # height checking
        for dir in dirs:
            newR = row + dir[0]
            newC = col + dir[1]

            # ! 범위 설정이 중요하다. 0 도 포함되어야 한다. 범위에 아니면 row == 0, col == 0 은 전부 dfs 탐색 에서 제외된다.
            if 0 <= newR < len(heights) and 0 <= newC < len(heights[0]) and atVisited[newR][newC] == False:

                if heights[newR][newC] >= heights[row][col]:
                    res = AtDFS(newR, newC)
                    if res:
                        return True

        return res

    # pacVisited = [[False for _ in range(len(heights[0]))]
    #                       for _ in range(len(heights))]

    # atVisited = [[False for _ in range(len(heights[0]))]
    #                      for _ in range(len(heights))]

    # start from the row of pacific ocean and atlantic ocean,
    # record the possibility in the pacVisited and atVisited (which is done in DFS function)
    for i in range(len(heights[0])):
        pacDFS(0, i)
        AtDFS(len(heights)-1, i)

    # start from the column of pacific ocean and atlantic ocean,
    # record the possibility in the pacVisited and atVisited (which is done in DFS function)
    for i in range(len(heights)):
        pacDFS(i, 0)
        AtDFS(i, len(heights[0])-1)

    # visited 배열은 따로 필요가 없다.
    # 어느 길로 가던 도착만 하면 됨.
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            canReachPac = pacVisited[i][j]
            canReachAt = atVisited[i][j]

            print(canReachPac, canReachAt, i, j)
            if canReachAt and canReachPac:
                result.append([i, j])

    print(result)

# pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
#                 2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])


# pacificAtlantic_v2([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    #  2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
# pacificAtlantic([[2, 3, 5], [3, 2, 2]])


approaches = Enum("app", "BFS DFS DFS_STACK")
APPROACH = approaches.BFS
APPROACH = approaches.DFS
APPROACH = approaches.DFS_STACK

""" Idea: We are not gods. We can't let it rain and see where the water goes.

But as humans we can search from the beach up the mountains, and only travel to
mountains where water can go down, i.e higher mountains than the current ones.
and if starting from some beach of the pacific and some beach of the atlantic
and ultimately land you on the same mountain then rain fall on that mountian
will go to both oceans """


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        if APPROACH == approaches.BFS:
            print("BFS")
            return self.pacificAtlantic_BFS(heights)
        elif APPROACH == approaches.DFS:
            print("DFS")
            return self.pacificAtlantic_DFS(heights)
        elif APPROACH == approaches.DFS_STACK:
            print("DFS stack")
            return self.pacificAtlantic_DFS_STACK(heights)

    def pacificAtlantic_DFS_STACK(self, heights: List[List[int]]) -> List[Tuple[int]]:
        # initialization of beaches near the ocean to start searching
        num_rows = len(heights)
        num_cols = len(heights[0])
        pacific_beaches, atlantic_beaches = [], []

        for i in range(num_cols):
            pacific_beaches.append((0, i))
            atlantic_beaches.append((num_rows - 1, i))

        for i in range(num_rows):
            pacific_beaches.append((i, 0))
            atlantic_beaches.append((i, num_cols - 1))

        def dfs(stack: List[Tuple[int]]) -> set:
            flowed = set()
            while stack:
                cur = stack.pop()
                flowed.add(cur)

                row, col = cur
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_row, next_col = row + x, col + y

                    if (
                        next_row < 0
                        or num_rows <= next_row
                        or next_col < 0
                        or num_cols <= next_col
                        or (next_row, next_col) in flowed
                    ):
                        continue
                    if heights[next_row][next_col] >= heights[row][col]:
                        stack.append((next_row, next_col))

            # Note usually the stack implementation should loop through all node
            # that is not visited, in case there are unconected parts of the
            # graph that should be searched. But here we have initialize all the
            # nodes to care about in the stack so we don't need to loop agian.
            return flowed

        pacific_flowed = dfs(pacific_beaches)
        atlantic_flowed = dfs(atlantic_beaches)
        return list(pacific_flowed.intersection(atlantic_flowed))

    def pacificAtlantic_DFS(self, heights: List[List[int]]) -> List[Tuple[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])
        pacific_beaches, atlantic_beaches = [], []

        for i in range(num_cols):
            pacific_beaches.append((0, i))
            atlantic_beaches.append((num_rows - 1, i))

        for i in range(num_rows):
            pacific_beaches.append((i, 0))
            atlantic_beaches.append((i, num_cols - 1))

        def dfs(beaches: List[Tuple[int]]) -> set:
            flowed = set()

            def dfs_util(cur: Tuple) -> None:
                flowed.add(cur)
                row, col = cur
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_row, next_col = row + x, col + y

                    if (
                        next_row < 0
                        or num_rows <= next_row
                        or next_col < 0
                        or num_cols <= next_col
                        or (next_row, next_col) in flowed
                    ):
                        continue
                    if heights[next_row][next_col] >= heights[row][col]:
                        dfs_util((next_row, next_col))

            for beach in beaches:
                if beach not in flowed:
                    dfs_util(beach)

            return flowed

        pacific_flowed = dfs(pacific_beaches)
        atlantic_flowed = dfs(atlantic_beaches)
        return list(pacific_flowed.intersection(atlantic_flowed))

    def pacificAtlantic_BFS(self, heights: List[List[int]]) -> List[Tuple[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific_q, atlantic_q = Queue(), Queue()

        # initializing all the node from the ocean
        for i in range(num_cols):
            pacific_q.put((0, i))
            atlantic_q.put((num_rows - 1, i))

        for i in range(num_rows):
            pacific_q.put((i, 0))
            atlantic_q.put((i, num_cols - 1))

        def bfs(queue: Queue) -> set:
            flowed = set()
            while not queue.empty():
                row, col = queue.get()
                flowed.add((row, col))

                # check for all four directions
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_row, next_col = row + x, col + y

                    if (
                        next_row < 0
                        or num_rows <= next_row
                        or next_col < 0
                        or num_cols <= next_col
                        or (next_row, next_col) in flowed
                    ):
                        continue

                    if heights[next_row][next_col] >= heights[row][col]:
                        queue.put((next_row, next_col))
            return flowed

        pacific_flowed = bfs(pacific_q)
        atlantic_flowed = bfs(atlantic_q)

        return list(pacific_flowed.intersection(atlantic_flowed))


sol = Solution()
a = sol.pacificAtlantic(
    [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
)
print(a)
