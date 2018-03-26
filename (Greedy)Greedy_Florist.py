#!/bin/python3
import sys

def getMinimumCost(n, k, c):
    result = [[]]
    level = 0
    num_of_each_level = 0
    for i in range(n):
        if num_of_each_level >= k:
            level += 1
            num_of_each_level = 0
            result.append([])
        price = (level + 1) * c[i]
        result[level].append(price)
        num_of_each_level += 1
    return sum([sum(each) for each in result])

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, sorted(c, reverse = True))
print(minimumCost)