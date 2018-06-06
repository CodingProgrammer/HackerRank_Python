#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def cal_median(arr):
    length = len(arr)
    arr = sorted(arr)
    if length % 2 != 0:
        return arr[length // 2]
    return (arr[length // 2] + arr[length // 2 - 1]) / 2 

def activityNotifications(expenditure, d):
    ans = 0
    for i in range(d, len(expenditure)):
        median = cal_median(expenditure[i-d:i])
        if expenditure[i] >= 2 * median:
            ans += 1
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
