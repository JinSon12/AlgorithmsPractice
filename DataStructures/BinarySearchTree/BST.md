# Binary Search Tree 

참고: http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html 

이진 탐색 트리를 구현하려면, 먼저 그 재료가 되는 `Node` class 정의해야 함. 
`Node` class : self.data, self.left, self.right 존재. 
초기회 = 데이터 값만 주고, 좌, 우 노드는 비어있다. 

```
class Node(object): 
  def __init__(self, data) -> None:
      self.data = data 
      self.left = self.right = None
  
``` 

### Initializing an Empty Tree 
```
class BinarySearchTree(object): 
  def __init__(self) -> None:
      self.root = None 
``` 