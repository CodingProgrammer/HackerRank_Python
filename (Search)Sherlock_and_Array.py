#!/bin/python3

import sys


def solve(n, a):
    sum_left = 0
    sum_rigth = sum(a[1:])
    if sum_left == sum_rigth:
        return 'YES'
    for i in range(1, n):
        sum_left += a[i-1]
        sum_rigth -= a[i]
        if sum_left == sum_rigth:
            return 'YES'
    return 'NO'

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(n, a)
    print(result)
