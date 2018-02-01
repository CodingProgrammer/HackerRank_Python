'''
1. sort the list
2. iterate the list, find the difference between the elements which next to each other, and make the difference the key of bucket.
3. following the 2nd step, record the index while creating keys
4. sort the keys of the bucket, the values related to the minimum keys are the index wanted.
'''
#!/bin/python3

import sys

def closestNumbers(arr):
    bucket = {}
    arr = sorted(arr)
    for i in range(0, len(arr) - 1):
        k = str(arr[i + 1] - arr[i])
        # ' ' are needed to record the correct index
        bucket[k] = bucket.get(k, '') + str(i) +' '+ str(i + 1) + ' '
    for k in sorted(bucket, key = int):
        # as you add the the index in string format, so you need split to get correct index
        for inside_k in bucket[k].split():
            print(arr[int(inside_k)], end = ' ')
        break

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)