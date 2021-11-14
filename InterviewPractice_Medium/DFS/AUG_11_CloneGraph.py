# https://leetcode.com/problems/clone-graph/

"""
133. Clone Graph


"""

from collections import deque
from InterviewPractice_Medium.DFS.Node import Node
from typing import Deque


class Solution:

    # 36ms ~ 40ms, 78 ~ 60%
    def cloneGraph_BFS_Iterative(self, node: 'Node') -> 'Node':
        if not node:
            return node

        res = {node: Node(node.val)}
        queue = Deque([node])

        while queue:
            n = queue.popleft()

            for neigh in n.neighbors:

                # 만약 neigh가 새로운 그래프에 없다면, (방문하지 않은 노드이면)
                # 큐에 추가하고 (neigh 의 이웃을 확인하기 위해)
                # 또, res 딕셔너리에 새로운 노드 neigh 를 만들고, val 추가.
                if neigh not in res:
                    queue.append(neigh)
                    res[neigh] = Node(neigh.val)

                # 1) 방문하지 않은 neigh 를 res 에 추가했거나
                # 2) 이미 방문 한 neigh 라도 (2 -> 3, 4 -> 3)
                # 이웃으로 추가해야 한다.
                res[n].neighbors.append(res[neigh])

        return res[node]

    # 28 ~ 40ms, 60 ~ 98%
    def cloneGraph_DFS_Iterative(self, node: 'Node') -> 'Node':
        if not node:
            return node

        res = {node: Node(node.val)}

        stack = [node]

        while stack:

            n = stack.pop()
            for neigh in n.neighbors:

                if neigh not in res:
                    res[neigh] = Node(neigh.val)
                    stack.append(neigh)

                res[n].neighbors.append(res[neigh])

        return res[node]

    # slower than the above two
    def cloneGraph_DFS_recursive(self, node: 'Node') -> 'Node':
        mapping = {}

        def recursion(node):

            if not node:
                return

            if node in mapping:
                clone_node = mapping[node]
                return clone_node

            else:
                clone_node = Node(node.val, [])
                mapping[node] = clone_node

            for neighbor in node.neighbors:
                clone_node.neighbors.append(recursion(neighbor))

            return clone_node

        return recursion(node)

    def cloneGraph_NOV2021(self, node: 'Node') -> 'Node':
        if not node:
            return node

        res = {node: Node(node.val)}

        def BFS():
            q = deque([node])

            while q:
                n = q.popleft()

                for neigh in n.neighbors:
                    if neigh not in res:
                        q.append(neigh)
                        res[neigh] = Node(neigh.val)

                    res[n].neighbors.append(res[neigh])
        BFS()
        return res[node]
