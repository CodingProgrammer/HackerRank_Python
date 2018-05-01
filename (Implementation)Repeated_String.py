#!/bin/python3

import sys

def repeatedString(s, n):
    quotient, remainder = divmod(n, len(s))
    return quotient * (s.count('a')) + s[:remainder].count('a')

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)