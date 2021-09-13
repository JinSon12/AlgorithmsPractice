"""
ABCDE 


Key Insight: 
DFS 할 시에 더 이상 갈 곳이 없다면, 
재귀에서 빠져나오게 되는데 
이때 방문한 노드를 미방문으로 다시 바꾸어 주어야 한다 
- 그렇지 않으면, 새로운 노드에서 방문하였던 곳을 방문하고 싶어도 방문할 수가 없다. 
- 자세한 것은 노트 참조. 

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N)]
visited = [0] * N


def isFriends():
    def dfs(pos, count):
        if count == 4:
            return True

        visited[pos] = 1
        # print(visited, count)

        res = False
        for neigh in graph[pos]:
            if visited[neigh] == 0:
                # print(neigh, pos)
                res = dfs(neigh, count + 1)
                if res:
                    return True
                visited[neigh] = 0

    for i in range(N):
        # visited = [0] * N        visited 배열을 초기화 하는 대신, 방문을 미방문으로 바꾸어 주는 것이 더 효율적이다.
        res = dfs(i, 0)
        visited[i] = 0

        if res:
            return 1

    return 0


# for generating graph
for _ in range(M):
    a, b = map(int, input().rstrip().split())

    graph[a].append(b)
    graph[b].append(a)

print(isFriends())


def v2():
    n, m = map(int, input().split())
    arr = [[] for i in range(n)]
    visited = [False] * n  # 모든 노드 방문X

    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)  # a가 b랑 친구인것은
        arr[b].append(a)  # b가 a랑 친구인것과 같다 # 둘은 친구사이

    def dfs(d, v):
        if d == 4:  # A, B, C, D, E 모두 만족 = 깊이가 4
            print(1)
            exit()
        for i in arr[v]:
            if not visited[i]:  # 방문하지 않았을때 실행
                visited[i] = True  # 방문처리
                dfs(d+1, i)
                visited[i] = False

    # 처음부터 마지막 노드까지 해당 깊이까지 들어가는 것이 있는지 탐색
    for i in range(n):
        visited[i] = True
        dfs(0, i)
        visited[i] = False
