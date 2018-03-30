#!/bin/python3

import sys
from itertools import combinations
def angryChildren(k, arr):
    # Complete this function
    new_comb = combinations(arr, k)
    
    temp_result = [max(each) - min(each) for each in new_comb]

    return min(temp_result)

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = angryChildren(k, arr)
    print(result)