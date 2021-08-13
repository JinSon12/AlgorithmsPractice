"""
11725. 트리의 부모 찾기

https://www.acmicpc.net/problem/11725

"""

import collections
import sys

input = sys.stdin.readline

nNodes = int(input())  # num nodes

parents = [0 for _ in range(nNodes + 1)]

# making the tree
tree = [[] for _ in range(nNodes + 1)]

for _ in range(nNodes - 1):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

# print(tree)


def bfs():
    queue = collections.deque([1])
    parents[1] = 1

    while queue:
        node = queue.popleft()
        print("node", node)

        for neigh in tree[node]:
            if parents[neigh] == 0:
                parents[neigh] = node

                queue.append(neigh)

    return parents


bfs()


# dfs 로도 해 보기.
def dfs():
    pass


for i in range(2, len(parents)):
    print(parents[i])
