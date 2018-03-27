#!/bin/python3

import sys

def largestPermutation(n, k, arr):
    num_swap = 0
    for i in range(n):
        if num_swap >= k:
            break

        if arr[i] < max(arr[i:]):
            num_swap += 1
            max_key = arr.index(max(arr[i:]))
            arr[i], arr[max_key] = arr[max_key], arr[i]
    return arr



if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = largestPermutation(n, k, arr)
    print (" ".join(map(str, result)))