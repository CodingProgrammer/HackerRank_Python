#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0
    for i in range(len(q)):
        if (q[i] - (i + 1)) > 2:
            return 'Too chaotic'
        for j in range(i + 1, len(q)):
            if q[j] < q[i]:
                q[i], q[j] = q[j], q[i]
                ans += 1

    return ans

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
