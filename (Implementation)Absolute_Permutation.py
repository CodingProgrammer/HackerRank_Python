#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    position = set([i for i in range(1, n + 1)])
    new_permutation = []
    for i in range(1, n + 1):
        if ((k + i) in position) and ((i - k) in position):
            new_permutation.append(min(k + i, i - k))
            position.remove(min(k + i, i - k))
        elif (k + i) in position:
            new_permutation.append(k + i)
            position.remove(i + k)
        elif (i - k) in position:
            new_permutation.append(i - k)
            position.remove(i - k)
        else:
            return [-1]
    return new_permutation

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
