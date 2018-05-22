#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A, H, W):
    to_reduce = []
    total = 6 * (sum([sum(row) for row in A]))
    for i in range(H):
        for j in range(W):
            left, right, up, down = 0, 0, 0, 0
            #left
            if 0 <= j - 1 < W:
                left = min(A[i][j], A[i][j - 1])
            #right
            if 0 <= j + 1 < W:
                right = min(A[i][j], A[i][j + 1])
            #up
            if 0 <= i - 1 < H:
                up = min(A[i][j], A[i - 1][j])
            #down
            if 0 <= i + 1 < H:
                down = min(A[i][j], A[i + 1][j])

            to_reduce.append(left + right + up + down)
            to_reduce.append((A[i][j] - 1) * 2)
    return (total - sum(to_reduce))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A, H, W)

    fptr.write(str(result) + '\n')

    fptr.close()
