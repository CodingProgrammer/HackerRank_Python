'''
return the steps happened in Insertion Sort algorithm
'''
#!/bin/python3

import sys

def runningTime(arr):
    # Complete this function
    step = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        while temp < arr[i - 1] and i > 0:
            arr[i] = arr[i - 1]
            i -= 1
            step += 1
        arr[i] = temp
    return (step)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)
