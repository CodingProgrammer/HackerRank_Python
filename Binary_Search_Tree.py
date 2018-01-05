class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root == None:
            return -1
        else:
            height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            return height

T = 9
l = [20, 50, 35, 44, 9, 15, 62, 11, 13]
myTree = Solution()
root = None
for i in range(T):
    data = l[i]
    root = myTree.insert(root,data)
height = myTree.getHeight(root)
print(height)  