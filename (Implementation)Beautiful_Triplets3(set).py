#!/bin/python3

import sys

def beautifulTriplets(d, arr):
    set_arr = set(arr)
    ans = [1 for each in arr if ((each + d) in set_arr and (each + 2 * d) in set_arr)]
    return len(ans)
         

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)
