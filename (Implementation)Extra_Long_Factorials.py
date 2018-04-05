#!/bin/python3

import sys

def extraLongFactorials(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print (result)
    
if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
