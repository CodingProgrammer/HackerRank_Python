'''
This is a LinkedList class and some of the methods useful
These methods contain:
InitList,  GetLength, is_Empty, Clear, Append, Display, Display, GetItem, Index, Insert, Delete

2018/01/07: The real change on a LinkedList sequence happen to .next(that means the pointer), the 
change on curent(like: current = current.netx) just to iterate the LinkedList.

2018/01/10:
1. next is a build-in function, so ues next_ 
2. Next()--- a generator. Make it possible to iterate the Linkedlist outside the LList class
'''
class Node:
    def __init__(self,data,next_ = None):
        self.data = data
        self.next = next_

class LinkList:
    def __init__(self):
        self._head = None
    
    def __str__(self):
        current = self._head
        while current:
            print(current.data, end = ' ')
            current = current.next
        return ""
 
    def InitList(self,data):
        self._head = Node(data[0])
        current = self._head
        for i in data[1:]:
            new_node = Node(i)
            current.next = new_node
            current = current.next

    def GetLength(self):
        count = 0
        current = self._head
        while current != None:
            current = current.next
            count += 1
        return count

    def is_Empty(self):
        return self.GetLength() == 0

    def Clear(self):
         self._head = None

    def Append(self,item):     
        if self._head == None:
            self._head = Node(item)
            return 
        else:
            current = self._head
            while current.next != None:
                current = current.next
            current.next = Node(item)
    def Display(self):
        current = self._head
        print('The data in LinkList are:', end = ' ')
        while current != None:
            print(current.data, end = ' ')
            current = current.next
        print(sep = ' ')            # to print a \n
    def GetItem(self, index):
        if self.GetLength() == 0:
            print('The LinkList is empty!', end = ' ')
        j = 0
        current = self._head
        while current.next != None and j < index:
            current = current.next
            j += 1
        if j == index:
            return current.data
        else:
            print('There is no such item in this LinkList!')
    def Index(self, value):
        if self.GetLength() == 0:
            print('The LinkList is empty!')
        j = 0
        current = self._head
        while current.next and current.data != value:
            current = current.next
            j += 1
        if current.data == value:
            return j
        else:
            print('The value %d has not been found in this LinkList!' %(value))
    def Insert(self, index, value):
        if self.GetLength() == 0 or index < 0 or index > self.GetLength():
            return -1
        new_node = Node(value)
        if index == 0:
            new_node.next = self._head
            self._head = new_node
        
        else:
            current = self._head
            previous = current
            while current.next != None and self.Index(current.data) != index:
                previous = current
                current = current.next
            if self.Index(current.data) == index:
                new_node.next = current
                previous.next = new_node
                #current = new_node
            '''     
            while current.next:      #replace 90 ~ 100 by 82 ~ 88
                if self.Index(current.data) == index:
                    new_node.next = current
                    previous.next = new_node
                    current = new_node
                previous = current
                current = current.next 
            if self.Index(current.data) == index:     # for case: index == len(LinkList) - 1
                new_node.next = current
                previous.next = new_node
                current = new_node  
            '''         

    def Delete(self,index):
        if self._head == None:
            raise ValueError('The LinkedList is empty, can NOT Delete!')
        if index < 0 or index > self.GetLength():
            raise ValueError('Out of range!')
        if index == 0:
            self._head = self._head.next
        else:
            current = self._head
            previous = current
            while current.next != None and self.Index(current.data) != index:
                previous = current
                current = current.next
            if self.Index(current.data) == index:
                previous.next = current.next
    def Pop(self):
        if self._head == None:
            raise ValueError('Empty LinkedList!')
        current = self._head
        previous = current
        if current.next == None:
            e = current.data
            self._head = None
            return e
        while current.next:
            previous = current
            current = current.next
        previous.next = current.next

    def Delete_Dupliactes(self):
        if self._head == None:
            return None
        current = self._head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def Next(self):
        if self._head == None:
            raise StopIteration
        current = self._head
        while current:
            yield current.data
            current = current.next
'''    
l1 = LinkList()
f = l1.Next()
print(next(f))
l1.InitList([1, 2, 3, 4, 5])
l1.Display()
l1.Pop()
l1.Display()
f = l1.Next()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
'''