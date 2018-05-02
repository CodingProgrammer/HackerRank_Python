#!/bin/python3

import os
import sys
from collections import Counter

def happyLadybugs(b, n):
    b_counter = Counter(b)
    for each_key in b_counter:
        if each_key != '_' and b_counter[each_key] < 2: 
            return ('NO')

    if len(b) == 1 and b != '_':
        return 'NO'
    if len(b) == 2 and b[0] != b[1]:
        return 'NO'
    if '_' not in b:    
        for i in range(1, n - 1):
            if b[i] != b[i + 1] and b[i - 1] != b[i]:
                return "NO"
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())
    
    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b, n)

        fptr.write(result + '\n')

    fptr.close()
