'''
Need not to compare all the string, make correct termination conditions
'''
#!/bin/python3
import sys

def funnyString(s):
    # Complete this function
    r = s[::-1]
    length = len(s)
    for i in range(1, length // 2 + 1):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return 'Not Funny'
    return 'Funny'
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)