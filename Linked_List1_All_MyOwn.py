'''
Inheritate from Linked_List_All_MyOwn
add self_rear and it make the Append method's time complexity O(1) 
'''

import Linked_List_All_MyOwn
class Linkedlist1(Linked_List_All_MyOwn.LinkList):
    def __init__(self):
        super().__init__()
        self._rear = None

    def InitList(self, data):
        self._head = Linked_List_All_MyOwn.Node(data[0])
        current = self._head
        for i in data[1:]:
            new_node = Linked_List_All_MyOwn.Node(i)
            current.next = new_node
            current = current.next
        self._rear = current
        
    
    def Append(self, data):
        if self._head == None:
            self._head = Linked_List_All_MyOwn.Node(data)
            self._rear = self._head
            return
        self._rear.next = Linked_List_All_MyOwn.Node(data)
        self._rear = self._rear.next
