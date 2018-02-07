#!/bin/python3

import sys

def diagonalDifference(a, n):
    # Complete this function
    sum_zhu = 0
    sum_fu = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                sum_zhu += a[i][j]
            if i + j == n -1 :
                sum_fu += a[i][j]
    return abs(sum_zhu - sum_fu)
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a,n)
    print(result)