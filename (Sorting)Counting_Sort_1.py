'''
Awesome use of Bucket(dict)
'''

#!/bin/python3

import sys

def countingSort(arr):
    # Complete this function
    bucket = dict.fromkeys([str(each) for each in range(0, 100)], 0)
    for key in arr:
        bucket[key] = bucket.get(key, 0) + 1
    for key in sorted(bucket, key = int):
        print(bucket[key], end = ' ')


if __name__ == "__main__":
    n = int(input().strip())
    arr = input().strip().split(' ')
    result = countingSort(arr)
    #print (" ".join(map(str, result)))