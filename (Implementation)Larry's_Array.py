Algorithm:https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A, n):
    inversions = 0
    for i in range(n - 1):
        inversions += sum([1 if (A[i] > A[j]) else 0 for j in range(i , n)])
    if inversions % 2 == 0:
        return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A, n)

        fptr.write(result + '\n')

    fptr.close()
