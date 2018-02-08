#!/bin/python3

import sys

def plusMinus(arr, n):
    n_positive = 0
    n_negative = 0
    n_zeros = 0
    for each in arr:
        if each > 0:
            n_positive += 1
        elif each < 0 :
            n_negative += 1
        else:
            n_zeros += 1
    print('%.6f' %(n_positive / n))
    print('%.6f' %(n_negative / n))
    print('%.6f' %(n_zeros / n))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr,n)