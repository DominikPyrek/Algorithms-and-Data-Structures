class Binary_Tree:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def addNode(self, data):
        if data == self.data: 
            return
        if data < self.data:
            if self.left:
                self.left.addNode(data)
            else:
                self.left = Binary_Tree(data);
        if data > self.data:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = Binary_Tree(data);
    
    def traverseTree(self):
        nums = []
        if self.left:
            nums += self.left.traverseTree()

        nums.append(self.data)

        if self.right:
            nums += self.right.traverseTree()
        
        return nums

    #def searchNode(self, data):

x = Binary_Tree(2)
x.addNode(3)
x.addNode(1)

print(x.traverseTree())

