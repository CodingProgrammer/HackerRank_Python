#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr, n):
    if arr == sorted(arr):
        return 'yes'
    index_i, index_j = 0, 0
    #find the out-most index 
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i+1]:
            index_i = i
            break
    
    for j in range(len(arr) - 1, 0, -1):
        if arr[j] < arr[j-1]:
            index_j = j
            break  
    
    #swap
    swap_arr = arr.copy()
    swap_arr[index_i], swap_arr[index_j] = swap_arr[index_j], swap_arr[index_i]
    if swap_arr == sorted(swap_arr):
        print('yes')
        print('swap', index_i + 1, index_j + 1)
        return
    
    #reverse
    reverse_arr = arr.copy()
    reverse_arr[index_i:index_j+1] = reverse_arr[index_i:index_j+1][::-1]
    if reverse_arr == sorted(arr):
        print('yes')
        print('reverse', index_i+1, index_j+1)
        return
    else:
        return 'no'

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = almostSorted(arr, n)
    
    if result:
        print(result)
