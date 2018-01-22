'''
Algorithm: Compare the element with the elements before it and find the index to insert, move all the elements backward after the index.
Timie complexity: O(n^2)
Stability : Stable
'''
#!/bin/python3
import sys
def insertionSort2(n, arr):
    # Complete this function
    for i in range(1, n):
        temp = arr[i]
        while temp < arr[i - 1] and i > 0:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = temp
        print(' '.join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
