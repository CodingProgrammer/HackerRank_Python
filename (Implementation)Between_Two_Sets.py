#!/bin/python3

import sys

def getTotalX(a, b):
    n = 0
    for i in range(max(a), min(b) + 1):
        flag = True
        for each_a in a:
            if i % each_a != 0:
                flag = False
                break
        for each_b in b:
            if each_b % i != 0:
                flag = False
                break
        if flag == True:
            n += 1
    return n

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)