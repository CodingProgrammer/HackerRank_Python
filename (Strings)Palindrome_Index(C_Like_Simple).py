#!/bin/python3

import sys

def palindromeIndex(s):
    # Complete this function
    length = len(s)
    for i in range(0, length // 2):
        if s[i] != s[length - i - 1]:
            if s[i + 1] == s[length - i - 1] and s[i + 2] == s[length - i - 2]:
                return i
            else:
                return length - i - 1
    return -1

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)