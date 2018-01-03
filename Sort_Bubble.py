#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
sum_num = 0
for i in range(n):
    each_num = 0
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            each_num += 1
    sum_num += each_num
    if each_num == 0:                    #each_num == 1 is wrong, like 2, 3, 1. Just after swap(3, 1), this is one step, then (the sequence now is 2, 1, 3) can process swap(2, 1)
        break
print('Array is sorted in {} swaps.'.format(sum_num))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))