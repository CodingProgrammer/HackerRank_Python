#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q, n):
    step = 0
    flag = True
    
    for k in range(n):
        if q[k] - (k + 1) > 2:
            return 'Too chaotic'
        
    for i in range(n):
        if flag == False:
            break
        flag = False
        for j in range(1, n - i):
            if q[j] < q[j - 1]:
                q[j], q[j - 1] = q[j - 1], q[j]
                step += 1
                flag = True
                
    return step
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q, n))
