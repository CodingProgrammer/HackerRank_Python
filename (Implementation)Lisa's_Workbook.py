#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 0
    ans = 0
    for each_chapter in range(n):
        page += 1
        for num_problem in range(1, arr[each_chapter] + 1):
            if num_problem == page:
                ans += 1
            if num_problem % k == 0 and num_problem != arr[each_chapter]:
                page += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
