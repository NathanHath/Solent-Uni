class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def recursiveInsert(self, new_value):
        if new_value < self.value :
            if self.left is None:
                self.left = TreeNode(new_value)
            else:
                self.left.recursiveInsert(new_value)
        else:
            if self.right is None:
                self.right = TreeNode(new_value)
            else:
                self.right.recursiveInsert(new_value)



    def recursivePrint(self):
        print(f"### LOG: calling recursivePrint() on node with value {self.value}")
        if self.left is not None:
            self.left.recursivePrint()
        print(self.value)
        if self.right is not None:
            self.right.recursivePrint()
        print(f"### LOG: leaving recursivePrint() on node with value {self.value}")

