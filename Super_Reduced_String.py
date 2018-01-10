'''
This one like the leetcode one '{[()]}'
use  stack to judege whether the next pre-input equal to the last one in the stack
if next pre-input == stack[-1]: stack.pop()
else: stack.append(next pre-input)
'''

def super_reduced_string(s):
    mystack = []
    for c in s:
        if len(mystack) == 0:
            mystack.append(c)
        else:
            if c == mystack[-1]:
                mystack.pop()
            else:
                mystack.append(c)
    if len(mystack) == 0:
        return 'Empty String'
    return ''.join(mystack)
s1 = 'aa'
print(super_reduced_string(s1))