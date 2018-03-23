#!/bin/python3

import sys

def toys(w, n):
    w = sorted(w)
    min_weight = w[0]
    level = 1
    for each in w:
        if each <= min_weight + 4:
            continue
        else:
            min_weight = each
            level += 1
    return level
    

if __name__ == "__main__":
    n = int(input().strip())
    w = list(map(int, input().strip().split(' ')))
    result = toys(w, n)
    print(result)