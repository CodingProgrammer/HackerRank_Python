#!/bin/python3
import sys
arr = []
l_hourglass_sum = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
def hourglass_sum(start_row, end_row, start_col, end_col, A):
    sum_numbers = 0
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            sum_numbers += A[i][j]
    sum_numbers = sum_numbers - A[start_row + 1][start_col] - A[start_row + 1][end_col]
    l_hourglass_sum.append(sum_numbers)
for i in range(0,4):
    for j in range(0,4):
        hourglass_sum(i, i + 2, j, j + 2, arr)

print(max(l_hourglass_sum))