#!/bin/python3

import sys

def icecreamParlor(m, arr):
    res = []
    for first in range(len(arr) - 1):
        for second in range(first + 1, len(arr)):
            if (arr[first] + arr[second]) == m:
                res.append(first + 1)
                res.append(second + 1)
                return res
                
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))
