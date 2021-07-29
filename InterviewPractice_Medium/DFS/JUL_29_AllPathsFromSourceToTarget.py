from typing import List


# https://leetcode.com/problems/all-paths-from-source-to-target/


"""
797. All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Key Insight: 
- dfs (recursively), until we find the exit (n-1) node, and return the pathSoFar

"""


class Solution:

    # 88 ms, 99.25%
    # 15.7 MB, less than 44.96%
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # len(graph)-1 b/c last node is going to be the exit node.
        # i.e. in len(graph) == 5, there are 5 nodes, but the count starts from 0-4
        graph_len = len(graph) - 1
        res = []
        path = [0]

        def dfs(node, pathSoFar):
            # from line 8, if last node, we want to append the pathSoFar to res.
            if node == graph_len:
                res.append(pathSoFar)
                return

            for i in graph[node]:
                dfs(i, pathSoFar + [i])

        dfs(0, path)
        return res


stn = Solution()
print(stn.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
