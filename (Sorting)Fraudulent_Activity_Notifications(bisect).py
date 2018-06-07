#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
# Complete the activityNotifications function below.
def get_median(arr, n):
	if n % 2 != 0:
		return arr[n // 2]
	return (arr[n // 2] + arr[n // 2 - 1]) / 2
	
def activityNotifications(expenditure, d):
	ans = 0
	sorted_slice = sorted(expenditure[:d])
	if expenditure[d] >= 2 * get_median(sorted_slice, d):
		ans += 1

	for i in range(d + 1, len(expenditure)):
		index_2remove = bisect.bisect_left(sorted_slice, expenditure[i - d - 1])
		sorted_slice.pop(index_2remove)
		bisect.insort(sorted_slice, expenditure[i - 1])
		median = get_median(sorted_slice, d)
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
