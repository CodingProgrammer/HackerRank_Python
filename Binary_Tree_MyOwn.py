'''
Q: Is that ok to make isSameTree a class func?
'''
class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left 
        self.right = right

class Tree:
    def __init__(self):
        self.root = Node()

    def add(self, value):
        new_node = Node(value)
        if self.root.value == None:
            self.root = new_node
        
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:
                treeNode = myQueue.pop(0)
                if treeNode.left == None:
                    treeNode.left = new_node
                    return
                elif treeNode.right == None:
                    treeNode.right = new_node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)
    def Pre_Order_Recurse(self, root):
        if root == None:
            return
        print(root.value)
        self.Pre_Order_Recurse(root.left)
        self.Pre_Order_Recurse(root.right)
    def Mid_Order_Recurse(self, root):
        if root == None:
            return
        self.Mid_Order_Recurse(root.left)
        print(root.value)
        self.Mid_Order_Recurse(root.right)    
    def Later_Order_Recurse(self, root):
        if root == None:
            return
        self.Later_Order_Recurse(root.left)
        self.Later_Order_Recurse(root.right)
        print(root.value)

    def Pre_Order_Iterate(self, root):
        if root == None:
            return
        else:
            myStack = []
            treeNode = root
            while treeNode or myStack:
                while treeNode:
                    print(treeNode.value)
                    myStack.append(treeNode)
                    treeNode = treeNode.left
                treeNode = myStack.pop()
                treeNode = treeNode.right

    def Mid_Order_Iterate(self, root):
        if root == None:
            return
        else:
            myStack = []
            treeNode = root
            while treeNode or myStack:
                while treeNode:
                    myStack.append(treeNode)
                    treeNode =treeNode.left
                treeNode = myStack.pop()
                print(treeNode.value)
                treeNode = treeNode.right
    def isSymmetric_Recurse(self):
        def isSym(left, right):
            if left and right and left.value == right.value:
                return isSym(left.left, right.right) and isSym(left.right, right.left)
            return left is right            #terminal judgement
        return isSym(self.root, self.root)
    
    def isSymmetric_Iterate(self, root):    #awesome
        queue = [root]
        while queue:
            val = [i.value if i else None for i in queue]
            if val != val[::-1]: return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True

def isSameTree(p, q):  #This is not a class method, you can just put the two different root into the func, and it wil tell you whether they are the same tree
    if p and q:
        return p.value == q.value and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return p is q

    


t1 = Tree()
t2 = Tree()
t1.add(0)
t1.add(2)
t1.add(21)
t2.add(0)
t2.add(2)
t2.add(2)

print(t1.isSymmetric_Iterate(t1.root))

#print(isSameTree(t1.root, t2.root))