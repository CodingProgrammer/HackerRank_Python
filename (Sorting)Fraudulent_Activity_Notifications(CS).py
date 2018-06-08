#!/bin/python3

import math
import os
import random
import re
import sys
	
def activityNotifications(arr, n, d):
	ans = 0
	window = [0 for _ in range(201)]
	for i in range(d):
		window[arr[i]] += 1
	if d % 2 != 0:
		odd = True
		median_count = d // 2 + 1
	else:
		median_count_l = d // 2
		median_count_r = d // 2 + 1
		odd = False

	for j in range(n - d):
		count_current = 0
		if odd:
			for k in range(201):
				count_current += window[k]
				if count_current >= median_count:
					median = k
					break
		
		else:
			median_l, median_r = 0, 0
			for k in range(201):
				count_current += window[k]
				if median_l == 0 and count_current >= median_count_l:
					median_l = k
				if median_r == 0 and count_current >= median_count_r:
					median_r = k 
				if median_l and median_r:
					median = (median_l + median_r) / 2
					break
			
		if arr[j + d] >= 2 * median:
			ans += 1

		window[arr[j]] -= 1
		window[arr[j + d]] += 1

	return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, n, d)

    fptr.write(str(result) + '\n')

    fptr.close()
