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
    
    def levelOrder_Iteration(self, root):
        if root == None:
            return 
        else:
            myqueue = []
            myqueue.append(root)
            while myqueue:
                node = myqueue.pop(0)
                if node:
                    print(node.data, end = ' ')
                    if node.left:
                        myqueue.append(node.left)
                    if node.right:
                        myqueue.append(node.right)

    def levelOrder_Recursion(self, root):
        ans = []
        def preOrder(root, level):
            if root:
                if len(ans) < level + 1:
                    ans.append([])
                ans[level].append(root.data)       #change the sequence here can get pre_order, mid_order
                preOrder(root.left, level + 1)
                preOrder(root.right, level + 1)
        preOrder(root, 0)
        print(ans)
T = 9
l = [20, 50, 35, 44, 9, 15, 62, 11, 13]
myTree = Solution()
root = None
for i in range(T):
    data = l[i]
    root = myTree.insert(root,data)
height = myTree.getHeight(root)
print(height)  
myTree.levelOrder_Iteration(root)
myTree.levelOrder_Recursion(root)