'''
Linked_Circle_List make the time complexity of prepend and append methos O(1) 
Methods: initlist, get_length, is_empty, clear, prepend, append, pop, index, insert, printall
'''
class Node:
    def __init__(self,data,next_ = None):
        self.data = data
        self.next = next_

class LCList:
    def __init__(self):
        self._rear = None

    def initlist(self, data):
        for each in data[:]:
            self.append(each)
    
    def get_length(self):
        if self.is_empty():
            return 0
        current = self._rear.next
        i = 1
        while current != self._rear:
            i += 1
            current = current.next
        return i

    def is_empty(self):
        return self._rear == None

    def clear(self):
        self._rear = None

    def prepend(self, data):
        new_node = Node(data)
        if self._rear == None:
            new_node.next = new_node
            self._rear = new_node
            return 
        new_node.next = self._rear.next
        self._rear.next = new_node

    def append(self, data):
        #self.prepend(data)
        new_node = Node(data)
        if self._rear == None:
            new_node.next = new_node
            self._rear = new_node
            return
        new_node.next = self._rear.next
        self._rear.next = new_node
        #update self._rear
        self._rear = new_node

    def pop(self, index):
        if self._rear == None:
            raise AttributeError('The list is empty!')
        if index < 0 or index > self.get_length() - 1:
            raise AttributeError('Index out of range!')
        current = self._rear.next
        previous = self._rear
        temp = self._rear
        while current != self._rear and self.index(current.data) != index:
            previous = current
            current = current.next
        #when find the index want to pop
        if self.index(current.data) == index:
            #the element pop not the last, just make the previous point to the next.next
            previous.next = current.next
            #when you want to pop the last element, you also need to update the self._rear
            if current == self._rear:
                self._rear = previous
        return temp.data

    def index(self, data):
        if self.is_empty():
            raise AttributeError('The list is empty, please insert data first!')
        current = self._rear.next
        i = 0
        while current != self._rear and current.data != data:
            current = current.next
            i += 1
        if current.data == data:
            return i
        else:
            raise AttributeError('No such value in this list!')
        
    #unfinished
    def insert(self, index, data):
        if index < 0 or index > self.get_length() :
            raise AttributeError('Index to insert out of range!')
        if index == 0:
            self.prepend(data)
            return
        if index == self.get_length():
            self.append(data)
            return
        current = self._rear.next
        previous = current
        while current != self._rear:
            if self.index(current.data) == index:
                break
            previous = current
            current = current.next
        new_node = Node(data)
        new_node.next = current
        previous.next = new_node
        


    def printall(self):
        if self._rear == None:
            raise AttributeError('The list is empty!')
        current = self._rear.next
        while current != self._rear:
            print(current.data)
            current = current.next
        print(current.data)
l1 = LCList()
l1.initlist([0, 1, 2, 3])
#l1.printall()
l1.pop(3)
l1.printall()