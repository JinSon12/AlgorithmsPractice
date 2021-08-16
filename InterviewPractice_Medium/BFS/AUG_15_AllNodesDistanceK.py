# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

"""
863. All Nodes Distance K in Binary Tree

Key Insight : 
- convert binary tree -> graph 
- do a BFS from the target node for k levels

"""

from collections import deque


class Solution:
    # 28ms, 98%
    def distanceK_v2_BFS_fastest(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        res = []

        def bfsBuild(root):
            queue = deque([root])

            while queue:
                n = queue.popleft()
                nval = n.val

                if n.left:
                    leftval = n.left.val
                    graph[nval].append(leftval)
                    graph[leftval].append(nval)
                    queue.append(n.left)

                if n.right:
                    rightval = n.right.val
                    graph[nval].append(rightval)
                    graph[rightval].append(nval)
                    queue.append(n.right)

        def bfsFind(target, k):
            visitedlen = max(len(graph), max(graph))
            visited = [0] * (visitedlen + 1)
            visited[target] = 1

            queue = deque([(target, 0)])    # nodeNum, dist

            while queue:
                n, dist = queue.popleft()

                if dist == k:
                    res.append(n)

                for neigh in graph[n]:
                    # print(neigh, visited, res)
                    if visited[neigh] == 0:
                        visited[neigh] = 1
                        queue.append((neigh, dist + 1))

        bfsBuild(root)

        if len(graph) == 0 and k == 0:
            return [root.val]

        elif len(graph) == 0 and k != 0:
            return []

        bfsFind(target.val, k)

        return res

    # slightly slower
    def distanceK_v1_BFS_usingSet(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        res = []

        def bfsBuild(root):
            queue = deque([root])

            while queue:
                n = queue.popleft()
                nval = n.val

                if n.left:
                    leftval = n.left.val
                    graph[nval].append(leftval)
                    graph[leftval].append(nval)
                    queue.append(n.left)

                if n.right:
                    rightval = n.right.val
                    graph[nval].append(rightval)
                    graph[rightval].append(nval)
                    queue.append(n.right)

        def bfsFind(target, k):
            visited = set({target})
            queue = deque([(target, 0)])    # nodeNum, dist

            while queue:
                n, dist = queue.popleft()

                if dist == k:
                    res.append(n)

                for neigh in graph[n]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh, dist + 1))

        bfsBuild(root)
        bfsFind(target.val, k)

        return res
