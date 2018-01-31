'''
Divide-And-Conquer algorithm
'''
#!/bin/python3

import sys

def quickSort(arr):
    # Complete this function
    p = [arr[0]]
    left = []
    right = []
    for each in arr[1:]:
        if each > p[0]:
            right.append(each)
        else:
            left.append(each)
    return (left + p +right)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))