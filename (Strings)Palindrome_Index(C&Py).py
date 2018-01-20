'''
Use iteration but need not creat new-string every time
When s[i] != s[length - i - 1] that means the suspect character either s[i] or s[length - i - 1], so creat a new-string now without s[i], if the new string is Palindrome, return i, otherwise return length -i - 1
'''
#!/bin/python3

import sys

def palindromeIndex(s):
    # Complete this function
    length = len(s)
    for i in range(0, length // 2):
        if s[i] != s[length - i - 1]:
            new_s = s[:i] + s[i + 1:]
            if new_s == new_s[::-1]:
                return i
            else:
                return length - i - 1
    return -1

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
