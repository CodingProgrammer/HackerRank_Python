#!/bin/python3

import sys
arr = []
l_hourglass_sum = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
ans = []
for i in range(4):
    for j in range(4):
        ans.append(sum(arr[i][j : j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j : j + 3]))
print(max(ans))


'''
sum(arr[i + 2][j : j + 3])
DO NOT FORGET sum(), or there will be an error 'can only concatenate list (not "int") to list'
'''