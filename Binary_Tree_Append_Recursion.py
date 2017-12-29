class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def append(self,head,data): 
        #Complete this method
        if head == None:
            return Node(data)
        elif head.next == None:
            head.next = Node(data)
        else:
            self.append(head.next, data)
        return head