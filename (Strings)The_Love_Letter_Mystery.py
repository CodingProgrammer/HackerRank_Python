#!/bin/python3

import sys

def theLoveLetterMystery(s):
    # Complete this function
    if s == s[::-1]:
        return 0
    length = len(s)
    res = 0
    for i in range(0, length // 2):
        if s[i] != s[length - i - 1]:
            res += abs(ord(s[i]) - ord(s[length - i - 1]))
    return res
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)