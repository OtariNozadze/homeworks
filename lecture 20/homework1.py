
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


    def printLeafs(self):
        print("The Leafs Are")
        self._printLeafs(self.root)
    
    def _printLeafs(self, node):
        if node:
            if not node.left and not node.right:
                print(node.key, " ", end="")
            self._printLeafs(node.left)
            self._printLeafs(node.right)





        
        

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
binary_tree.printLeafs()