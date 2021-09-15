"""
토마토 

Key Insight: 

- BFS 를 완료하고 난 다음의 graph 의 상태는 [1, 0 ,-1] 이 섞여 있을 것이다. 
- 이때 nested for loop 을 사용해서 graph 에서 0 이 있는 것을 확인 할 수도 있지만, 
- 이것은 시간 소요를 증가시킬 것이다 (technically, runtime would be O(n^2))

- 따라서, counter 변수를 사용해서, 이때까지 익은 토마토의 갯수를 저장하고 
- possible_tomatoes 변수를 사용해서, 익을 수 있는 토마토의 갯수를 저장한다. (즉, 모든 토마토의 수에서 -1 토마토를 뺀다)
- possible_tomatoes 는 다시 말해 0 인 토마토의 갯수를 저장하는 변수. 

- counter 변수는 
- 새로운 0 토마토가 1로 바뀔 때 마다 1 씩 증가한다. 즉 익은 토마토의 갯수를 저장하는 변수이다. (이것은 days 변수와는 명확히 다르다)
- days 변수는 다음에 방문할 토마토들에 대해 일괄적으로 같은 숫자이고, 다음 세트를 방문할때 1씩 증가하지만, 
- count 변수는 새로운 토마토를 발견할 때 마다, 그 전의 갯수에서 +1 을 한다 

- count 변수는 1인 토마토를 포함하지 않는다. 오직 도달할 수 있는 0 -> 1로 바뀌는 토마토만을 기록한다. 
- 따라서 도달할 수 없는 0 토마토는 count 변수에 포함되지 않을 것이며, 
- 이로 인해 possible_tomatoes 와 차이가 생길 "수" 있게 된다. 
- 이 차이 가 있다면, 도달하지 못한 토마토가 있으므로 -1 을 반환한다. 
- 없다면, 모든 토마토에 도달 할 수 있다는 뜻이므로, max_days 를 반환한다. 

"""
from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().rstrip().split())) for _ in range(M)]
q = deque([])
dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]


def findMinDays():
    global counter
    max_days = 0

    while q:
        r, c, days = q.popleft()

        for x, y in dirs:
            newr = r + x
            newc = c + y

            if 0 <= newr < M and 0 <= newc < N and graph[newr][newc] == 0:
                graph[newr][newc] = 1
                q.append([newr, newc, days + 1])
                max_days = days + 1
                counter += 1

    return max_days if counter == possible_tomatoes else -1


counter = 0
possible_tomatoes = N * M
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            q.append([i, j, 0])
            counter += 1
        elif graph[i][j] == -1:
            possible_tomatoes -= 1


print(findMinDays())


# 5-- ms
def fasterSolution():
    import sys
    from collections import deque

    m, n = map(int, sys.stdin.readline().split())
    maze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def bfs():
        while tomato:
            a, b = tomato.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 > nx or nx >= n or 0 > ny or ny >= m:
                    continue
                if maze[nx][ny] == 0:
                    maze[nx][ny] = maze[a][b] + 1
                    tomato.append((nx, ny))

    tomato = deque()

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                tomato.append((i, j))
    ans = 0
    bfs()

    check = True
    for i in maze:
        for j in i:
            if j == 0:
                check = False
                break
        if check == False:
            break
        ans = max(ans, max(i))

    if check == True:
        print(ans-1)
    else:
        print(-1)
