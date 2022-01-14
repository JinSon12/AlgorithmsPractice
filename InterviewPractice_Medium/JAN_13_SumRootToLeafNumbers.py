# https://leetcode.com/problems/sum-root-to-leaf-numbers/
""" 
종료 조건은 
- 노드가 없을때 (부모 노드는 있지만, 부모 노드의 자식노드가 하나가 없을때), 
  이때, 0 을 반환한다. 
  (왜 발견한 숫자를 리턴하지 않냐면, 이때 리턴을 하면 자식노드가 하나도 없는 노드는 두번 숫자를 리턴받게 된다. 
   이는 최종적으로 더 큰 숫자가 되어 버린다)
- 노드가 있고, 자식 노드가 하나도 없을때: 
  이때는 이때까지 발견한 숫자를 모두 더해준다. 


"""


def sumNumbers_dfs(root):
    def dfs(node, pathSoFar):
        # 노드가 없을때
        if not node:
            return 0

        # 왼쪽 자식으로 부터 리턴받는 값
        newPath = pathSoFar * 10 + node.val

        # 자식 노드가 없을 때
        # 현재 노드에서 거쳐왔던 숫자를 반환한다.
        if not node.left and not node.right:
            return pathSoFar

        left = dfs(node.left, newPath)
        right = dfs(node.right, newPath)

        return left + right


def sumNumbers_bfs():
    pass
