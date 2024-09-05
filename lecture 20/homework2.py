class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def length(self):
        self.counter = 0
        self._length(self.root)
        return self.counter
    def _length(self, node):
        if node:
            if node.left:
                self.counter += 1
            if node.right:
                self.counter += 1
            self._length(node.left)
            self._length(node.right)



binary_tree = BinaryTree()
binary_tree.insert(10)
binary_tree.insert(15)
binary_tree.insert(9)
binary_tree.insert(6)
binary_tree.insert(17)
binary_tree.insert(12)
binary_tree.insert(1)
binary_tree.insert(29)
binary_tree.insert(7)
print(binary_tree.length())