'''
Double_Linked_List: 
creat new_node with correct prev and next_ can save a lot of energy
pay attention to the prepend and append methods
Methods:__init__, prepend, append, initlist, index, is_empty, getlength, pop, insert, printall
'''
class DLNode:
    def __init__(self, data, prev = None, next_ = None):
        self.data = data
        self.prev = prev
        self.next = next_

class DLList:
    def __init__(self):
        self._head = None
        self._rear = None
    
    def prepend(self, data):
        new_node = DLNode(data, None, self._head)
        if self._head == None:
            self._rear = new_node
        else:
            new_node.next.prev = new_node
        self._head = new_node

    '''
    # prepend method without using correct next_ to creat new_node
        if self._head == None:
            self._head = DLNode(data)
            #self._head.next = self._rear
            return
        new_node = DLNode(data)
        self._head.prev = new_node
        new_node.next = self._head
        self._head = new_node
        if self._rear == None:
            self._rear = self._head.next
    '''
    def append(self, data):
        new_node = DLNode(data, self._rear, None)
        if self._head == None:
            self._head = new_node
        else:
            new_node.prev.next = new_node
        self._rear = new_node

    def initlist(self, data):
        for each in data[:]:
            self.append(each)

    def index(self, data):
        current = self._head
        i = 0
        while current != None and current.data != data:
            current = current.next
            i += 1
        if current == None:
            raise ValueError('%d is not in list' %(data))
        if current.data == data:
            return i
    def is_empty(self):
        return self._head == None

    def getlength(self):
        if self.is_empty():
            return 0
        current = self._head
        i = 0
        while current != None:
            current = current.next
            i += 1
        return i   

    def pop(self, index_):
        if index_ < 0 or index_ > self.getlength() - 1:
            raise ValueError('Index out of range!')
        #pop the first element
        if index_ == 0:
            temp =self._head
            self._head.next.prev = None
            self._head = self._head.next
            return temp.data
        #pop the last element
        if index_ == self.getlength() - 1:
            temp = self._rear
            self._rear.prev.next = None
            self._rear = self._rear.prev
            return temp.data
        #pop the element between (first, last)
        current = self._head
        while current.next != None:
            if self.index(current.data) == index_:
                break
            current = current.next
        #if self.index(current.data) == index_:
        current.prev.next = current.next
        current.next.prev = current.prev
        return current.data

    def insert(self, index_, data):
        if index_ < 0 or index_ > self.getlength():
            raise ValueError('Index out of range!')
        #prepend
        if index_ == 0:
            self.prepend(data)
            return
        #append
        if index_ == self.getlength():
            self.append(data)
            return
        #insert at (first, last)
        current = self._head
        while current.next != None:
            if self.index(current.data) == index_:
                break
            current = current.next
        new_node = DLNode(data, current.prev, current)
        current.prev.next = new_node
        current.prev = new_node

    def printall(self):
        if self._head == None:
            raise AttributeError('The list is empty!')
        current = self._head
        while current:
            print(current.data, end = ' ')
            current = current.next
        print(sep = '')

l1 = DLList()
print(l1.getlength())
l1.pop(0)
l1.printall()
