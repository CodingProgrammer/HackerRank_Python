#!/bin/python3

import sys

def pickingNumbers(a):
    bucket = {}
    for each_key in set(a):
        bucket[str(each_key)] = 0
    for each_element in a:
        for each_key in bucket.keys():
            if each_element >= int(each_key) and abs(each_element - int(each_key)) <= 1:
                bucket[each_key] += 1

    return sorted(bucket.values(), reverse = True)[0]

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(sorted(a))
    print(result)
