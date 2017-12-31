'''
The difference between SinCycLinkedList and LinkedList is : 
The last element in SinCycLinkedList point to the head but the last element in LinkedList point to None

Operation defference:
SinCycLinkedList start with : current = self.head.next 
LinkedList start with: current = self.head
'''
class Node:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class SinCycLinkedlist:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
    def initlist(self, value):
        new_node = Node(value[0])
        new_node.next = self.head.next
        self.head.next = new_node
        for n in value[1:]:
            self.append(n)
    def add(self, value):                #add element from front
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def display(self):
        current = self.head.next
        while current != self.head:
            print(current.data)
            current = current.next
        #print(sep = ' ')
    def search(self, value):
        current = self.head.next
        while current != self.head:
            if current.data == value:
                return True
            current = current.next
        return False
    def empty(self):
        return self.head.next == self.head
    def size(self):
        count = 0
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count 
    def remove(self, value):
        current = self.head.next
        previous = self.head
        while current != self.head:
            if current.data == value:
                previous.next = current.next
                current = current.next
            previous = current
            current = current.next
    def append(self, value):
        new_node = Node(value)
        current = self.head.next
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
    def index(self, value):
        count = 0
        current = self.head.next
        while current != self.head:
            if current.data != value:
                count += 1
                current = current.next
            else:
                break
        return count               
    def insert(self, index, value):
        if index < 0 or index > self.size():
            return -1
        new_node = Node(value)
        current = self.head.next
        previous = self.head
        while current != self.head:
            if self.index(current.data) == index:
                new_node.next = current
                previous.next = new_node
                current = new_node
            previous = current
            current = current.next
    def pop(self):
        if self.empty():
            raise AttributeError ('The SinCycLinkedList is empty!')
        current = self.head.next
        previous = self.head
        while current.next != self.head:
            previous = current
            current = current.next
        previous.next = self.head
l1 = SinCycLinkedlist()
l1.initlist([1, 2, 3])
l1.display()
l1.pop()
l1.pop()
l1.pop()

l1.display()