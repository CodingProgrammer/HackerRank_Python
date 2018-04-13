#!/bin/python3

import os
import sys
def pageCount(n, p):
    total_turn = n // 2
    step_from_1 = p // 2
    return min(step_from_1, total_turn - step_from_1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
