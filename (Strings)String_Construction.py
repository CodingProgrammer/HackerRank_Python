#!/bin/python3
import sys
def stringConstruction(s):
    # Complete this function
    p = ''
    money = 0
    for c in s:
        if c not in p:
            p += c
            money += 1
        else:
            p += c
    return money
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
