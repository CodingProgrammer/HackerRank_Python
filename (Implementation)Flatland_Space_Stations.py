#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(c, m, n):
    ans = set()
    for i in range(m - 1):
        ans.add((c[i + 1] - c[i]) // 2)
    ans.add(0)
    ans.add(c[0] - 0)
    ans.add(n - 1 - c[-1])
    return (max(ans))
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(sorted(c), m, n)

    fptr.write(str(result) + '\n')

    fptr.close()
