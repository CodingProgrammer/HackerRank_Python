class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
 
    def InitList(self,data):
        self.head = Node(data[0])
        current = self.head
        for i in data[1:]:
            new_node = Node(i)
            current.next = new_node
            current = current.next

    def GetLength(self):
        count = 0
        current = self.head
        while current != None:
            current = current.next
            count += 1
        return count

    def is_Empty(self):
        return self.GetLength() == 0

    def Clear(self):
         self.head = None

    def Append(self,item):     
        if self.head == None:
            return Node(item)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(item)
    def Display(self):
        current = self.head
        print('The data in LinkList are:', end=' ')
        while current != None:
            print(current.data, end = ' ')
            current = current.next
        print(sep = ' ')
    def GetItem(self, index):
        if self.GetLength() == 0:
            print('The LinkList is empty!')
        j = 0
        current = self.head
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
        current = self.head
        while current.next and current.data != value:
            current = current.next
            j += 1
        if current.data == value:
            return j
        else:
            print('The value %d has not been found in this LinkList!' %(value))
    def Insert(self, index, value):
        if self.GetLength() == 0 or index < 0 or index > self.GetLength():
            return None
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            current = self.head
            previous = current
            while current.next:
                if self.Index(current.data) == index:
                    new_node.next = current
                    previous.next = new_node
                    current = new_node
                previous = current
                current = current.next 
            if self.Index(current.data) == index:
                new_node.next = current
                previous.next = new_node
                current = new_node           

l1 = LinkList()
l1.InitList([1, 2, 3, 4, 5])
l1.Display()
l1.Insert(4,6)
l1.Display()