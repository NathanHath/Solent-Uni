from Tree_node import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root.recursiveInsert(data)

    def print(self):
        if self.root is not None:
            self.root.recursivePrint()



    def dfs(self):


    def bfs(self):
        pass