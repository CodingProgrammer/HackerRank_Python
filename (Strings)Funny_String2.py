'''
This version need not a additional string r
'''
#!/bin/python3

import sys

def funnyString(s):
    # Complete this function
    #r = s[::-1]
    length = len(s)
    for i in range(1, length // 2 + 1):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[length - i]) - ord(s[length - i - 1])):
            return 'Not Funny'
    return 'Funny'
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
