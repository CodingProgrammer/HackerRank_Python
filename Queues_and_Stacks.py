'''
A stack is a data structure that uses a principle called Last-In-First-Out (LIFO), 
meaning that the last object added to the stack must be the first object removed from it. 

A queue is a data structure that uses a principle called First-In-First-Out (FIFO),
 meaning that the first object added to the queue must be the first object removed from it
'''
import sys
class Solution:
    # Write your code here
    def __init__(self):
        self.mystack = []
        self.myqueue = []

    def pushCharacter(self, data):
        self.mystack.append(data)

    def enqueueCharacter(self, data):
        self.myqueue.append(data)

    def popCharacter(self):
        return self.mystack.pop()

    def dequeueCharacter(self):
        return self.myqueue.pop(0)
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    