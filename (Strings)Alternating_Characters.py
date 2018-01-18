
'''
stack
'''
#!/bin/python3
import sys

def alternatingCharacters(s):
    # Complete this function
    mystack = s[0]
    for c in s[1:]:
        if c != mystack[-1]:
            mystack += c
    return len(s) - len(mystack)

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)