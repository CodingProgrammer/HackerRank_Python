#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    print(sum(arr) - max(arr), sum(arr) - min(arr))
   
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
