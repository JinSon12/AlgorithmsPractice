from collections import deque

n = int(input())
t1, t2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(t1):
    queue = deque([(t1, 0)])  # node number, level
    visited = set()
    res = [0]

    while queue:
        n, level = queue.popleft()

        visited.add(n)

        for neigh in graph[n]:
            if neigh not in visited:
                if neigh == t2:
                    print("neigh", neigh, t1, t2)
                    res.append(level + 1)
                queue.append((neigh, level + 1))

        if len(res) == 2:
            print(res[0], res[1])
            return abs(res[0] + res[1])

    return -1


print(bfs(t1))


# dfs (60ms faster than bfs)
visited = [False] * (n+1)

answer = -1


def dfs(t1, level):
    global visited, graph, b, answer
    visited[n] = True

    if n == t2:
        answer = level

    for i in range(len(graph[n])):
        if visited[graph[n][i]] == False:
            dfs(graph[n][i], level + 1)


dfs(t1, 0)
print(answer)
