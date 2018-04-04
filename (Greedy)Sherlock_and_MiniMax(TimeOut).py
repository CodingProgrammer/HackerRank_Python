#!/bin/python3

import sys


def sherlockAndMinimax(arr, p, q, n):
    bucket = {}
    for num in range(p, q+1):
        temp = set()
        if num not in arr:
            for each in arr:
                temp.add(abs(num - each))
            if str(min(temp)) not in bucket.keys():
                bucket[str(min(temp))] = [num]
            else:
                bucket[str(min(temp))].append(num)
    for each_key in sorted(bucket, key = int,reverse = True):
        return (bucket[each_key][0])
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    p, q = input().strip().split(' ')
    p, q = [int(p), int(q)]
    result = sherlockAndMinimax(arr, p, q, n)
    print(result)
