#!/bin/python3

import sys

def beautifulTriplets(d, arr):
    length = len(arr)
    ans = 0
    
    for i in range(length - 2):
        next_value = arr[i] + d
        nnext_value = arr[i] + 2 * d
        if next_value in arr[i + 1:]:
            index_next = arr.index(next_value)
            if nnext_value in arr[index_next + 1:]:
                ans += 1
    return ans
         

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)
