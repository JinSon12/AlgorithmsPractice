"""

Methods needed: 
- constructor, 
- insert(), 
- delete(), 
- find() 

"""


import Node


class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    # 재귀를 사용하여 insert()
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    # private, helper fn.
    def _insert_value(self, node, data) -> Node:
        if node is None:
            # initialize new Node
            node = Node.Node(data)

        # if a node already exists,
        # insert data on either the right and the left.
        # if the data to be inserted is greater than the root node, insert to the right, else left.
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)

        return node

    # find returns boolean value, True if a key exists in the BST, False if it doesn't
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None

        elif key < root.data:
            return self._find_value(root.left, key)

        else:
            return self._find_value(root.right, key)

    def remove(self, key):
        self.root, deleted = self._remove_value(self.root, key)
        return deleted

    def _remove_value(self, node, key):
        if node is None:
            return node, False

        # create the flag deleted, and set it to False
        deleted = False

        # 노드의 노드의 값과 키값이 같다면,
        if node.data == key:
            deleted = True

            # if there are left and right child nodes,
            if node.left and node.right:
                parent, child = node, node.right

                # find the left-most leaf node of the right child of the child node.
                while child.left is not None:
                    parent, child = child, child.left

                # by the time while loop finishes,
                # the left node of some child will be null.
                # we set the left of the child to the left subtree of the original node (the node to be deleted)
                child.left = node.left

                if parent != node:
                    # before we make the right node of the child to be the right node of the node,
                    # we have to make the left node of the parent to be the child's right node
                    # to make sure that we still have pointer to the right node of the child.
                    parent.left = child.right
                    child.right = node.right

                node = child

            # 자식 노드가 왼쪽이나 오른쪽 둘 중 하나의 곳에 있다면, 그냥 끌어올리기만 하면된다.
            elif node.left or node.right:
                node = node.left or node.right

            # 자식 노드가 없다.
            else:
                node = None

        # 키값이 노드의 data 보다 작다면,
        elif key < node.data:
            node.left, deleted = self._remove_value(node.left, key)

        # 키 값이 노드의 data 보다 크면, 우측으로 간다.
        else:
            node.right, deleted = self._remove_value(node.right, key)

        return node, deleted


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15))  # True
print(bst.find(17))  # False

# Delete
print(bst.remove(55))  # True
print(bst.remove(14))  # True
print(bst.remove(11))  # False
