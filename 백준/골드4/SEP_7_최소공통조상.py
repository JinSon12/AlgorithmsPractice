"""
최소 공통 조상. 

Lowest Common Ancestor algorithm. 

두 정점 u,v 에서 가장 가까운 공통 조상을 찾기. 

각 노드의 부모 노드를 모두 저장 한 뒤, 
루트노드에서부터 차례로 내려오면서 비교하여 
같지 않은 노드가 나올 때 까지 반복. 
처음으로 같지 않은 노드가 나왔을 때, 그 노드의 부모가 최소 공통 조상이다. 

반드시 리뷰

"""
import sys
input = sys.stdin.readline

TC = int(input())


def findLCA(u, v):

    u_parents = [u]
    v_parents = [v]

    # parents 배열에 노드 u,v 의 모든 조상을 저장하기.
    # 각 부모가 루트일때 까지 저장한다.
    while parents[u]:
        u_parents.append(parents[u])
        u = parents[u]        # u 는 자신의 직계 존속으로 바뀐다.

    while parents[v]:
        v_parents.append(parents[v])
        v = parents[v]

    # 이 시점에서 u_parents, v_parents 는 u, v 의 모든 부모를 저장했다.
    # 다음으로, 루트에서부터 자손으로 간다.
    # (마지막 부모에게서 자신으로 간다, 즉 parents 배열의 마지막 값인 루트의 값에서 ind 0 의 값인 자신에게께지 한칸씩 내려오면서 비교)
    # 자손이 다르다면, 그 자손의 직계 존속이 최소 공통 조상이다.
    u_height = len(u_parents) - 1
    v_height = len(v_parents) - 1

    while u_parents[u_height] == v_parents[v_height]:
        u_height -= 1
        v_height -= 1

    return (u_parents[u_height + 1])


for _ in range(TC):
    N = int(input())      # 총 노드 갯수

    parents = [0 for _ in range(N + 1)]     # 노드 갯수만큼 부모를 저장할 배열

    for _ in range(N-1):
        p, c = map(int, input().split())
        parents[c] = p                        # c 의 부모는 p 라고 parents 배열에 저장하기.

    # parents 배열은 완성 되었고,
    # 모든 노드에 대해서 그 노드의 부모를 저장한다.

    u, v = map(int, input().split())        # LCA 를 찾을 두 노드 입력 받기.

    print(findLCA(u, v))


def findLCA_set():
    def solution():
        n = int(input())
        parent = [0] * (n+1)

        for _ in range(n-1):
            a, b = map(int, input().split())
            parent[b] = a

        a, b = map(int, input().split())
        result = set()
        while parent[a] != a:
            result.add(a)
            a = parent[a]

        while b not in result:
            b = parent[b]

        print(b)

    T = int(input())
    for _ in range(T):
        solution()
