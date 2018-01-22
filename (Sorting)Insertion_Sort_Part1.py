#!/bin/python3
import sys
def insertionSort1(n, arr):
    # Complete this function
    temp = arr[-1]
    for i in range(n - 2, -1 , -1):
        if arr[i] > temp:
            arr[i + 1] = arr[i]
            print(' '.join(map(str, arr)))
            if i == 0:
                arr[i] = temp
                print(' '.join(map(str, arr)))
        else:
            arr[i + 1] = temp
            print(' '.join(map(str, arr)))
            break
'''
#another method use while loop
def insertionSort1(n, arr):
    # Complete this function
    temp = arr[-1]
    i = n - 2
    while arr[i] > temp and i >= 0:
        arr[i + 1] = arr[i]
        i -= 1
        print(' '.join(map(str, arr)))
    arr[i + 1] = temp 
    print(' '.join(map(str, arr))) 
'''
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)