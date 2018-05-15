#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    ans = 0
    count_odd = len([1 for each in B if each % 2 == 1])
    if count_odd % 2 == 1:
        return 'NO'

    for i in range(N):
        if B[i] % 2 == 1:
            if i == 0:
                B[i] += 1
                B[i + 1] +=1 
                ans += 2

            elif i == N - 1:
                B[i] += 1
                B[i - 1] += 1
                ans += 2

            else:    
                if B[i - 1] % 2 == 1:
                    B[i] += 1
                    B[i - 1] += 1
                    ans += 2
                else:
                    B[i] += 1
                    B[i + 1] +=1 
                    ans += 2
    
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
