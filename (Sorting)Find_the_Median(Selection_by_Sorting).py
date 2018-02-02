'''
sort and find the middle element
'''
#!/bin/python3

import sys

def findMedian(arr, n):
    # Complete this function
    arr.sort()
    return arr[(n - 1) // 2]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr, n)
    print(result)