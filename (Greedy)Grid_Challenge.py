#!/bin/python3

import sys

def gridChallenge(grid, n):
    for i in range(n):
        for j in range(n - 1):
            if grid[j][i] > grid[j + 1][i]:
                return 'NO'
    return 'YES'

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        grid = []
        grid_i = 0
        for grid_i in range(n):
            grid_t = str(input().strip())
            grid.append(sorted(grid_t))
        result = gridChallenge(grid, n)
        print(result)