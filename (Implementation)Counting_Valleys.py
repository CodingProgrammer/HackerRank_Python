#!/bin/python3

import sys

def countingValleys(n, s):
    level = 0
    num_vally = 0
    state = 0
    for each_c in s:
        if each_c == 'D':
            if state == 0:
                state = -1
            level -= 1
        else:
            if state == 0:
                state = 1
            level += 1
        if level == 0:
            if state == -1:
                num_vally += 1
            state = 0
    return (num_vally)

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
