"""
2606. 바이러스 

첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

7
6
1 2
2 3
1 5
5 2
5 6
4 7

"""

from sys import stdin
read = stdin.readline

d = {}

for i in range(int(read())):
    d[i+1] = set()  # 1 부터 시작한다. 왜냐하면 node 번호가 1번부터 있기 때문.

for j in range(int(read())):
    a, b = map(int, read().split())
    # 각각 노드에게 서로를 이웃으로 set 에 추가해준다.
    d[a].add(b)
    d[b].add(a)

# =====
visited = set({1})


def dfs(node, count):
    for neigh in d[node]:
        # print("curnode", node, "neigh", neigh, "count", count)
        if neigh not in visited:
            # print("curnode", node, "not visited neigh", neigh)
            visited.add(neigh)
            dfs(neigh, count + 1)


dfs(1, 0)
print(len(visited)-1)


# 좀 더 느린 편 ? 웹사이트에서는 느리다고 나옴.
# 메모리는 count 때문에 더 사용 될것.
def dfs_v2(node, count):
    for neigh in d[node]:
        # print("curnode", node, "neigh", neigh, "count", count)
        if neigh not in visited:
            # print("curnode", node, "not visited neigh", neigh)
            visited.add(neigh)
            count = dfs(neigh, count + 1)
    return count


print(dfs_v2(1, 0))
