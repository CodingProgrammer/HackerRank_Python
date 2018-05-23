#!/bin/python3

import math
import os
import random
import re
import sys

def cavityMap(grid, n):
    for i in range(n):
        for j in range(n):
            if 0 < i < n - 1 and  0 < j < n - 1:
                around = [grid[i - 1][j], grid[i][j - 1], grid[i][j + 1], grid[i + 1][j]]
                if all([1 if each < grid[i][j] else 0 for each in around]):
                    grid[i][j] = "X"
                    
    return ([''.join(each_row) for each_row in grid])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = [each for each in input()]
        grid.append(grid_item)

    result = cavityMap(grid, n)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
